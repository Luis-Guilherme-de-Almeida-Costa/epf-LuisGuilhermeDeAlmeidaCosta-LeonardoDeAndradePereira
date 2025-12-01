from controllers.user_controller import UserController
from controllers.pessoas_controller import PessoasController

def init_controllers(app):
    UserController(app)
    PessoasController(app)
