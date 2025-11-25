from bottle import Bottle
from config import Config
import bottle_mysql

class App:
    def __init__(self):
        self.bottle = Bottle()
        self.config = Config()
        self.setup_database()

    def setup_database(self):
        plugin = bottle_mysql.Plugin(
            dbuser=self.config.DB_USER,
            dbpass=self.config.DB_PASS,
            dbname=self.config.DB_NAME,
            dbhost=self.config.DB_HOST,
            dbport=self.config.DB_PORT
        )
        
        self.bottle.install(plugin)
        print("Plugin MySQL instalado com sucesso!")
    
    def setup_routes(self):
        from controllers import init_controllers

        print('🚀 Inicializa rotas!')
        init_controllers(self.bottle)


    def run(self):
        self.setup_routes()
        self.bottle.run(
            host=self.config.HOST,
            port=self.config.PORT,
            debug=self.config.DEBUG,
            reloader=self.config.RELOADER
        )


def create_app():
    return App()
