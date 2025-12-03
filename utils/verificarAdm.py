from bottle import request
from services.pessoas_service import PessoasService

class VerificarAdm:   
    def __init__(self):
        self._session = request.environ.get('beaker.session')
        self.pessoas_service = PessoasService()

    def verificarAdm(self, db, id_pessoa_adm):
        verificaAdm = self.pessoas_service.get_administrador_by_id(db, id_pessoa_adm)
        
        if not verificaAdm:
            return False
        else:
            return True