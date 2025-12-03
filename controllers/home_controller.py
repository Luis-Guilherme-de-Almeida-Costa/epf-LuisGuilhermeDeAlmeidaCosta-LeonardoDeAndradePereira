from bottle import Bottle, request, redirect
from .base_controller import BaseController
from services.filmes_service import FilmesService
from services.pessoas_service import PessoasService
from utils.verificarAdm import VerificarAdm
class HomeController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.filmes_service = FilmesService()
        self.pessoas_service = PessoasService()
        self.verificar_adm = VerificarAdm()        

    def setup_routes(self):
        self.app.route('/', method=['GET'], callback=self.index)
        self.app.route('/home', method=['GET'], callback=self.index_home)
        self.app.route('/home/search', method=['GET'], callback=self.index_search)
        self.app.route('/home/leitura/<id_filme>', method=['GET'], callback=self.index_leitura)
        self.app.route('/home/video/<id_filme>', method=['GET'], callback=self.index_video)

    def index(self, db):
        return self.render('homeSemLogin', path = "naoLogado", pathStatus = 'I', user=False, adm=False)
    
    def index_home(self, db):

        acao = self.filmes_service.get_by_category(db, "Ação")

        filme = self.filmes_service.get_all(db)

        session = request.environ.get('beaker.session')

        id_pessoa = session.get('user_id')

        pessoa = self.pessoas_service.get_by_id(db, id_pessoa)

        adm = self.verificar_adm.verificarAdm(db, id_pessoa)

        return self.render('homeComLogin', path = "logado", pathStatus = 'L', filmes = filme, user=pessoa, adm = adm, acao = acao, favoritos = None)
        
    def index_search(self, db):
        search_data = request.query.get('searchData')
         
        if not search_data:
            return redirect('/home')

        session = request.environ.get('beaker.session')

        id_pessoa = session.get('user_id')

        pessoa = self.pessoas_service.get_by_id(db, id_pessoa)

        filmes = self.filmes_service.get_by_name(db, search_data)

        adm = self.verificar_adm.verificarAdm(db, id_pessoa)

        return self.render('search', path = "logado", pathStatus = 'LI', filmes = filmes, user=pessoa, adm = adm)

    def index_leitura(self, db, id_filme):

        if not id_filme:
            return redirect('/home')

        session = request.environ.get('beaker.session')

        id_pessoa = session.get('user_id')

        pessoa = self.pessoas_service.get_by_id(db, id_pessoa)

        filme = self.filmes_service.get_by_id(db, id_filme)

        adm = self.verificar_adm.verificarAdm(db, id_pessoa)

        return self.render(
            'leitura',
            path="logado",
            pathStatus="LI",
            user=pessoa,
            adm=adm,
            filmes=filme
        )

    def index_video(self, db, id_filme):
        if not id_filme:
            return redirect('/home')

        session = request.environ.get('beaker.session')

        id_pessoa = session.get('user_id')

        pessoa = self.pessoas_service.get_by_id(db, id_pessoa)

        filme = self.filmes_service.get_by_id(db, id_filme)

        adm = self.verificar_adm.verificarAdm(db, id_pessoa)

        return self.render(
            'videoPlayer',
            path="logado",
            pathStatus="LI",
            user=pessoa,
            adm=adm,
            filmes=filme,
            video_path=filme['video_path']
        )