from bottle import Bottle, request, redirect # Importar 'redirect'
from .base_controller import BaseController
from services.pessoas_service import PessoasService
from utils.flash import FlashManager
from utils.verificarAdm import VerificarAdm
class PessoasController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.pessoas_service = PessoasService()
        self.verificar_adm = VerificarAdm()

    def setup_routes(self):
        self.app.route('/pessoas/add', method=['GET', 'POST'], callback=self.add_pessoa)
        self.app.route('/pessoas/login', method=['GET', 'POST'], callback=self.login_pessoa)
        self.app.route('/pessoas/edit', method=['GET', 'POST'], callback=self.edit_pessoa)
        self.app.route('/pessoas/logout', method=['GET', 'POST'], callback=self.delete_pessoa)


    def add_pessoa(self, db):
        flash = FlashManager()

        if request.method == 'GET':
            errors, success_message, form_data = flash.get_flash_messages()
            
            return self.render(
                'cadastro', 
                action="/pessoas/add", 
                path="naoLogado", 
                pathStatus='A', 
                user=False, 
                adm=False,
                errors=errors,
                data=form_data
            )
        
        else:
            current_data = {
                'nome': request.forms.get('nome', ''),
                'email': request.forms.get('email', ''),
                'cpf': request.forms.get('cpf', ''),
            }
            
            result = self.pessoas_service.save(db)
            
            if result['success']:
                return redirect('/pessoas/login')
            else:
                errors = result.get('error', {'geral': 'Erro desconhecido.'})
                flash.set_flash_errors_and_data(errors, current_data)
                return redirect('/pessoas/add')
    
    def login_pessoa(self, db):
        flash = FlashManager()
        
        if request.method == 'GET':
            
            errors, success_message, form_data = flash.get_flash_messages()
            
            return self.render(
                'login', 
                action="/pessoas/login", 
                path="naoLogado", 
                pathStatus='A', 
                user=False, 
                adm=False,
                errors=errors, 
                data=form_data
            )
        
        else:
            current_data = {
                'email': request.forms.get('email', ''),
            }

            result = self.pessoas_service.login(db)
            
            if result['success']:
                return redirect('/')
            else:
                errors = result.get('errors', {'geral': 'Erro de login desconhecido.'})
                flash.set_flash_errors_and_data(errors, current_data)
                return redirect('/pessoas/login')
    
    def edit_pessoa(self, db):
        flash = FlashManager()

        session = request.environ.get('beaker.session')

        id_pessoa = session.get('user_id')

        adm = self.verificar_adm.verificarAdm(db, id_pessoa)

        if request.method == 'GET':
            errors, success_message, form_data = flash.get_flash_messages()

            pessoa = self.pessoas_service.get_by_id(db, id_pessoa)
            if not pessoa:
                flash.set_flash_errors_and_data({"geral": "Usuário não encontrado."}, {})
                return redirect('/pessoas/logout')

            return self.render(
                'editarPerfil',              
                action="/pessoas/edit",
                errors=errors,
                success=success_message,
                path="logado",
                user=pessoa,
                adm=adm,
                pathStatus= 'LI'
            )

        else:
            current_data = {}
            result = self.pessoas_service.edit(db, id_pessoa)

            if result["success"]:
                flash.set_flash_success(["Usuário atualizado com sucesso!"])
                return redirect("/pessoas/edit")
            else:
                errors = result.get("errors", {"geral": "Erro ao atualizar usuário."})
                flash.set_flash_errors_and_data(errors, current_data)
                return redirect("/pessoas/edit")

    def delete_pessoa(self, db):
        self.pessoas_service.logout()
        return redirect('/')