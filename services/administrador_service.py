from bottle import request, redirect
from models.administrador import AdministradorModel
from utils.validate import ValidateFields
import bcrypt
class AdministradorService:
    def __init__(self):
        self.administrador_model = AdministradorModel()
        self.validate_fields = ValidateFields()

    def get_all(self, db):
        return self.administrador_model.get_all(db)
    
    def get_by_id_pessoa(self, db, id_pessoa):
        return self.administrador_model.get_by_id_pessoa(db, id_pessoa)

    def save(self, db, id_pessoa):

        novo_id = self.administrador_model.add_administrador(db, id_pessoa)
        
        if novo_id is None:
             return {'success': False, 'error': {'geral': 'Erro ao salvar no banco de dados.'}}

        return {'success': True, 'id': novo_id}