from bottle import request
from models.pessoas import PessoasModel, Pessoas
import bcrypt

class PessoasService:
    def __init__(self):
        self.pessoa_model = PessoasModel()

    def get_all(self, db):
        return self.pessoa_model.get_all(db)

    def login(self, db):
        nome = request.forms.get()

    def save(self, db):
        name = request.forms.get('nome')
        email = request.forms.get('email')
        cpf = request.forms.get('cpf')
        situacao = "A"
        senha = request.forms.get('senha')
        confirmarSenha = request.forms.get('confirmarSenha')
        exists = self.pessoa_model.get_by_email(db, email)

        if senha != confirmarSenha:
            return {'success': False, 'error': 'As senhas não coincidem!'}

        if exists:
            return {'success': False, 'error': 'Email já cadastrado!'}
        
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        pessoa = Pessoas(name=name, email=email, cpf=cpf, situacao=situacao, senha=senha_hash)
        novo_id = self.pessoa_model.add_pessoa(db, pessoa)

        return {'success': True, 'id': novo_id}

    def get_by_id(self, db, pessoa_id):
        return self.pessoa_model.get_by_id(db, pessoa_id)

    def edit_user(self, db):
        pessoa_id = request.forms.get('id')
        pessoa = self.pessoa_model.get_by_id(db, pessoa_id)

        if not pessoa:
            return {'success': False, 'error': 'Usuário não encontrado.'}

        pessoa.name = request.forms.get('nome')
        pessoa.email = request.forms.get('email')
        pessoa.cpf = request.forms.get('cpf')
        pessoa.situacao = request.forms.get('situacao')

        nova_senha = request.forms.get('senha')

        if nova_senha:
            pessoa.senha = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        self.pessoa_model.update_user(db, pessoa)
        return {'success': True}

    def delete_user(self, db, pessoa_id):
        self.pessoa_model.delete_user(db, pessoa_id)
        return {'success': True}
