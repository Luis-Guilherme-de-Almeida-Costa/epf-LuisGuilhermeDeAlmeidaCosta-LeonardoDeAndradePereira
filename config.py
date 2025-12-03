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
    DB_NAME = 'Cinema'
    DB_HOST = '172.29.12.36'
    DB_PORT = 3306
