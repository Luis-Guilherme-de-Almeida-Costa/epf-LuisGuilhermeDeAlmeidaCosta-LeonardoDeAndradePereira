from bottle import Bottle, request
from .base_controller import BaseController
from services.pessoas_service import PessoasService

class PessoasController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.pessoas_service = PessoasService()

    def setup_routes(self):
        self.app.route('/pessoas/add', method=['GET', 'POST'], callback=self.add_pessoa)
        self.app.route('/pessoas/login', method=['GET', 'POST'], callback=self.login_pessoa)
        self.app.route('/pessoas/edit/<pessoa_id:int>', method=['GET', 'POST'], callback=self.edit_pessoa)
        self.app.route('/pessoas/delete/<pessoa_id:int>', method='POST', callback=self.delete_pessoa)

    def add_pessoa(self, db):
        if request.method == 'GET':
            return self.render('cadastro', pessoa=None, action="/pessoas/add", path="naoLogado", pathStatus='A', user=False)
        else:
            self.pessoas_service.save(db)
            self.redirect('/pessoas/add')
    
    def login_pessoa(self, db):
        if request.method == 'GET':
            return self.render('cadastro', pessoa=None, action="/pessoas/add", path="naoLogado", pathStatus='A', user=False)
        else:
            self.pessoas_service.save(db)
            self.redirect('/home')

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
