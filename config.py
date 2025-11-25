import os

class Config:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Configurações do servidor
    HOST = 'localhost'
    PORT = 8080
    DEBUG = True
    RELOADER = True

    # Paths
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'views')
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    DATA_PATH = os.path.join(BASE_DIR, 'data')

    #Configuração do MySql
    DB_USER = 'root'
    DB_PASS = 'eqwefuijqiuofoiujqwfoijqwf-=--=c´çççqwedijiq9wi1ééé'
    DB_NAME = 'nome_do_banco'
    DB_HOST = '192.168.1.27'
    DB_PORT = 3306
