import os
import uuid # Para gerar nomes de arquivos únicos
from datetime import datetime
from .base_controller import BaseController
from bottle import request, redirect, Bottle
from services.pessoas_service import PessoasService
from services.filmes_service import FilmesService
from utils.flash import FlashManager
from utils.verificarAdm import VerificarAdm
from datetime import datetime, timedelta

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
        self.verificar_adm = VerificarAdm()
        

    def setup_routes(self):
        self.app.route('/filmes/store', method=['GET', 'POST'], callback=self.index_store)
        self.app.route('/filmes/remove', method=['GET'], callback=self.index_remove)
        self.app.route('/filmes/remove/<id_filme>', method=['POST'], callback=self.remove)

    def index_store(self, db):
        flash = FlashManager()

        session = request.environ.get('beaker.session')
        id_pessoa_adm = session.get('user_id')
        verificaAdm = self.pessoas_service.get_administrador_by_id(db, id_pessoa_adm)

        errors, success_message, form_data = flash.get_flash_messages()

        if not verificaAdm:
            flash.set_flash_errors_and_data({"geral": "Usuário não encontrado."}, {})
            return redirect('/pessoas/logout')

        pessoa = self.pessoas_service.get_by_id(db, id_pessoa_adm)

        if request.method == 'GET':
            return self.render('criaFilmes', 
                                path="logado", 
                                errors=errors, 
                                success=success_message, 
                                pathStatus= 'LI', 
                                action = "/filmes/store", 
                                adm = True,
                                user=pessoa,
                                data=form_data)
        else:
            errors = {}
            form_data = {}
            
            titulo = request.forms.get('titulo', '').strip()
            categorias_list = request.forms.getall('categorias')
            categoria = ",".join(categorias_list)
            data_exibicao_str = request.forms.get('data_exibicao', '').strip()
            sinopse = request.forms.get('sinopse', '').strip()
            diretor = request.forms.get('diretor', '').strip()

            form_data = {
                'titulo': titulo,
                'categoria': categoria,
                'sinopse': sinopse, 
                'diretor': diretor
            }
            
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
            status = 'ATIVO'
            
            if data_exibicao_str:
                try:
                    data_exibicao = datetime.strptime(data_exibicao_str, '%Y-%m-%dT%H:%M')
                    
                    agora_com_margem = datetime.now() + timedelta(seconds=5)

                    if data_exibicao > agora_com_margem:
                        status = 'AGENDADO'
                    elif data_exibicao <= agora_com_margem:
                        errors['data_exibicao'] = "A data e hora de exibição deve ser estritamente no futuro (mínimo 5 segundos de margem)."
                        flash.set_flash_errors_and_data(errors, form_data)
                        return redirect('/filmes/store')
                    
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
                'id_administrador': id_pessoa_adm,
                'sinopse': sinopse,
                'diretor': diretor
            }
    
            result = self.filmes_service.add_filme(db, filme_data)

            if result['success']:
                flash.set_flash_success(["Filme registrado com sucesso!"])
                return redirect('/filmes/store')
            else:
                errors_filme = result.get('errors')
                flash.set_flash_errors_and_data(errors_filme, form_data)
                if os.path.exists(capa_path): os.remove(capa_path)
                if os.path.exists(video_path): os.remove(video_path)
                return redirect('/filmes/store') 

    def index_remove(self, db):
        flash = FlashManager()

        session = request.environ.get('beaker.session')

        id_pessoa_adm = session.get('user_id')

        user = self.pessoas_service.get_by_id(db, id_pessoa_adm)

        adm = self.verificar_adm.verificarAdm(db, id_pessoa_adm)

        filme_list = self.filmes_service.get_all(db)

        if not adm:
            return redirect("/home")
    
        errors, success_message, form_data = flash.get_flash_messages()

        return self.render(
            'filmeRemover', 
            action="/adm/index", 
            path="logado", 
            pathStatus='L', 
            user=user, 
            adm=adm,
            filmes=filme_list,
            errors=errors,
            success=success_message
        )

    def remove(self, db, id_filme):
        flash = FlashManager()

        result = self.filmes_service.delete_filme(db, id_filme)
        
        if result['success']:
            flash.set_flash_success(["Filme removido com sucesso!"])
            return redirect('/filmes/remove')
        else:
            errors = result.get("errors", {"geral": "Erro ao atualizar filmes."})
            flash.set_flash_errors_and_data(errors, {})
            return redirect('/filmes/remove')