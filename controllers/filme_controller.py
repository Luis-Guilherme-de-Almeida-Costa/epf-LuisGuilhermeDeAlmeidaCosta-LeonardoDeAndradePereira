import os
import uuid # Para gerar nomes de arquivos únicos
from datetime import datetime
from .base_controller import BaseController
from bottle import request, redirect, Bottle
from services.pessoas_service import PessoasService
from services.filmes_service import FilmesService
from utils.flash import FlashManager


UPLOAD_DIR_CAPAS = 'static/uploads/capas/'
UPLOAD_DIR_VIDEOS = 'static/uploads/videos/'

os.makedirs(UPLOAD_DIR_CAPAS, exist_ok=True)
os.makedirs(UPLOAD_DIR_VIDEOS, exist_ok=True)


class FilmeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.pessoas_service = PessoasService()
        self.filmes_service = FilmesService()

    def setup_routes(self):
        self.app.route('/filmes/store', method=['GET', 'POST'], callback=self.index_store)

    def index_store(self, db):
        flash = FlashManager()

        session = request.environ.get('beaker.session')
        id_pessoa = session.get('user_id')
        pessoa = self.pessoas_service.get_by_id(db, id_pessoa)

        errors, success_message, form_data = flash.get_flash_messages()

        if not pessoa:
            flash.set_flash_errors_and_data({"geral": "Usuário não encontrado."}, {})
            return redirect('/pessoas/logout')

        if request.method == 'GET':
            return self.render('criaFilmes', 
                                path="logado", 
                                errors=errors, 
                                success=success_message, 
                                pathStatus= 'LI', 
                                action = "/filmes/store", 
                                user=pessoa,
                                data=form_data) //passar aqui depois

        else:

            errors = {}
            form_data = {}
            
            titulo = request.forms.get('titulo', '').strip()
            categoria = request.forms.get('categoria', '').strip()
            data_exibicao_str = request.forms.get('data_exibicao', '').strip()

            form_data = {
                'titulo': titulo,
                'categoria': categoria,
                'data_exibicao': data_exibicao_str
            }
            
            if not titulo:
                errors['titulo'] = "O título é obrigatório."
            if not categoria or categoria == 'Selecione uma categoria':
                errors['categoria'] = "A categoria é obrigatória."
            
            capa_upload = request.files.get('capa')
            video_upload = request.files.get('arquivo_video')

            if not capa_upload:
                errors['capa'] = "A capa do filme é obrigatória."
            elif capa_upload.content_type not in ['image/jpeg', 'image/png']:
                errors['capa'] = "Formato de capa inválido. Use JPG ou PNG."
                
            if not video_upload:
                errors['arquivo_video'] = "O arquivo de vídeo (MP4) é obrigatório."
            elif video_upload.content_type != 'video/mp4':
                errors['arquivo_video'] = "O vídeo deve estar no formato MP4."

            if errors:
                flash.set_flash_errors_and_data(errors, form_data)
                return redirect('/filmes/store')

            #agendamento
            data_exibicao = None
            agora = datetime.now()
            status = 'ATIVO'
            
            if data_exibicao_str:
                try:
                    data_exibicao = datetime.strptime(data_exibicao_str, '%Y-%m-%dT%H:%M')
                    
                    if data_exibicao > agora:
                        status = 'AGENDADO'
                    
                except ValueError:
                    errors['data_exibicao'] = "Formato de data e hora inválido."
                    flash.set_flash_errors_and_data(errors, form_data)
                    return redirect('/filmes/store')
                    
            capa_path = None
            video_path = None
            
            try:
                capa_filename = f"{uuid.uuid4()}_{capa_upload.filename}"
                video_filename = f"{uuid.uuid4()}_{video_upload.filename}"
                
                capa_path = os.path.join(UPLOAD_DIR_CAPAS, capa_filename)
                video_path = os.path.join(UPLOAD_DIR_VIDEOS, video_filename)

                capa_upload.save(capa_path) 
                video_upload.save(video_path)

            except Exception as e:
                print(f"Erro ao salvar arquivos: {e}")
                errors['geral'] = "Erro ao salvar os arquivos de mídia. Tente novamente."
                flash.set_flash_errors_and_data(errors, form_data)
                                
                return redirect('/filmes/store') 

            filme_data = {
                'titulo': titulo,
                'categoria': categoria,
                'data_exibicao': data_exibicao, 
                'status': status,
                'capa_path': capa_path.replace(os.path.sep, '/'), 
                'video_path': video_path.replace(os.path.sep, '/'),
                'id_usuario': id_pessoa
            }
            
            try:
                self.filmes_service.add_filme(db, filme_data)
                flash.set_flash_success({"Sucesso": "Filme registrado com sucesso! Status: " + status}, {})
                return redirect('/filmes/lista') 
            except Exception as e:
                print(f"Erro no BD ao inserir filme: {e}")
                
                if os.path.exists(capa_path): os.remove(capa_path)
                if os.path.exists(video_path): os.remove(video_path)
                
                errors['geral'] = 'Erro ao registrar filme no banco. Tente novamente.'
                flash.set_flash_errors_and_data(errors, form_data)
                return redirect('/filmes/store')