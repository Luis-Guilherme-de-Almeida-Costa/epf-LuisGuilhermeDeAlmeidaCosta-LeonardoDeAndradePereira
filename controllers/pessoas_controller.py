from bottle import Bottle, request, redirect # Importar 'redirect'
from .base_controller import BaseController
from services.pessoas_service import PessoasService
from utils.flash import FlashManager

class PessoasController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.pessoas_service = PessoasService()

    def setup_routes(self):
        self.app.route('/pessoas/add', method=['GET', 'POST'], callback=self.add_pessoa)
        self.app.route('/pessoas/login', method=['GET', 'POST'], callback=self.login_pessoa)


    def add_pessoa(self, db):


        flash = FlashManager()

        if request.method == 'GET':
            
            errors, form_data = flash.get_flash_messages()
            
            return self.render(
                'cadastro', 
                action="/pessoas/add", 
                path="naoLogado", 
                pathStatus='A', 
                user=False, 
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
            
            errors, form_data = flash.get_flash_messages()
            
            return self.render(
                'login', 
                action="/pessoas/login", 
                path="naoLogado", 
                pathStatus='A', 
                user=False, 
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
    
    def edit_pessoa(self, pessoa_id):
        pessoa = self.pessoas_service.get_by_id(pessoa_id)
        if not pessoa:
            return "Pessoa não encontrada"

        if request.method == 'GET':
            return self.render('pessoa_form', pessoa=pessoa, action=f"/pessoas/edit/{pessoa_id}")
        else:
            self.pessoas_service.edit_pessoa(pessoa)
            self.redirect('/pessoas')

    def delete_pessoa(self, pessoa_id):
        self.pessoas_service.delete_pessoa(pessoa_id)
        self.redirect('/pessoas')
