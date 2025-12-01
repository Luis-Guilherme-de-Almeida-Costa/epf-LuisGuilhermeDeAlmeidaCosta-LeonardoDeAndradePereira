from bottle import Bottle
from beaker.middleware import SessionMiddleware
from config import Config
from mysql_plugin import MySQLPlugin

class App:
    def __init__(self):
        self.bottle = Bottle()      # O app REAL
        self.config = Config()

        self.setup_database()
        self.setup_routes()

        # Aplica sessão APENAS no WSGI FINAL
        self.session_opts = {
            'session.type': 'file',
            'session.cookie_expires': 3600,
            'session.data_dir': './sessions',
            'session.auto': True
        }

        self.wsgi_app = SessionMiddleware(self.bottle, self.session_opts)

    def setup_database(self):
        plugin = MySQLPlugin(self.config)
        self.bottle.install(plugin)

    def setup_routes(self):
        from controllers import init_controllers
        init_controllers(self.bottle)   # <- sempre passe o BOTTLE real

    def run(self):
        from bottle import run
        run(
            app=self.wsgi_app,     # <- Aqui sim usamos o middleware
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
