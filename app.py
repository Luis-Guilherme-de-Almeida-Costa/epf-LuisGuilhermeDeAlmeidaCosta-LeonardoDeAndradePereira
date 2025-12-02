from bottle import Bottle
from beaker.middleware import SessionMiddleware
from config import Config
from mysql_plugin import MySQLPlugin
from plugins.auth_redirect_plugin import setup_auth_redirect

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()

        self.setup_database()
        self.setup_routes()

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
        setup_auth_redirect(self.bottle)
        
        from controllers import init_controllers
        init_controllers(self.bottle) 

    def run(self):
        from bottle import run
        run(
            app=self.wsgi_app,
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
