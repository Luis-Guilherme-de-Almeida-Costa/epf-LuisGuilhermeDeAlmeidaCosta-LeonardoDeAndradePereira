import mysql.connector
from bottle import PluginError

class MySQLPlugin:
    name = 'mysql'
    api = 2

    def __init__(self, config):
        self.config = config

    def setup(self, app):
        pass

    def apply(self, callback, route):
        def wrapper(*args, **kwargs):
            db = mysql.connector.connect(
                host=self.config.DB_HOST,
                user=self.config.DB_USER,
                password=self.config.DB_PASS,
                database=self.config.DB_NAME,
                port=self.config.DB_PORT,
                charset='utf8mb4',
                collation='utf8mb4_unicode_ci'
            )
            
            kwargs['db'] = db
            try:
                response = callback(*args, **kwargs)
            finally:
                db.close()
            return response
        return wrapper
