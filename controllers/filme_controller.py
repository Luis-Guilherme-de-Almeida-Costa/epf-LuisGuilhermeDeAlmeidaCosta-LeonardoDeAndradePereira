from bottle import Bottle, request
from .base_controller import BaseController
from services.pessoas_service import PessoasService

class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.pessoas_service = PessoasService()

    def setup_routes(self):
        self.app.route('/', method=['GET', 'POST'], callback=self.index)
        self.app.route('/home', method=['GET', 'POST'], callback=self.index_home)

    def index(self, db):
        if request.method == 'GET':
            return self.render('homeSemLogin', path = "naoLogado", pathStatus = 'I', user=False)
        else:
            return
    
    def index_home(self, db):
        if request.method == 'GET':
            return self.render('homeComLogin', path = "naoLogado", pathStatus = 'I', user=False)
        else:
            return
   
