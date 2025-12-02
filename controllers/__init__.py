from controllers.user_controller import UserController
from controllers.pessoas_controller import PessoasController
from controllers.home_controller import HomeController
from controllers.filme_controller import FilmeController

def init_controllers(app):
    UserController(app)
    PessoasController(app)
    FilmeController(app)
    HomeController(app)
