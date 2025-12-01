from bottle import request
from models.pessoas import PessoasModel, Pessoas
import bcrypt
from validators import email as validate_email, length, ValidationError
class PessoasService:
    def __init__(self):
        self.pessoa_model = PessoasModel()

    def get_all(self, db):
        return self.pessoa_model.get_all(db)
    


    def validate_fields(self, email, senha):
        errors = {}

        try:
            if not validate_email(email):
                errors['email'] = "Email inválido."
        except ValidationError:
            errors['email'] = "Email em formato inválido."

        try:
            length(senha, min=6)
        except ValidationError:
            errors['senha'] = "Senha deve ter pelo menos 6 caracteres."

        return errors

    def login(self, db):
        try:
            email = request.forms.get('email')
            senha = request.forms.get('senha')

            errors = self.validate_fields(email, senha)

            if errors:
                return {'success': False, 'errors': errors}

            user = self.pessoa_model.get_by_email(db, email)
            if not user:
                return {'success': False, 'errors': {'email': 'Usuário não cadastrado.'}}

            if not bcrypt.checkpw(senha.encode('utf-8'), user['senha_hash'].encode('utf-8')):
                return {'success': False, 'errors': {'senha': 'Senha incorreta.'}}

            session = request.environ.get('beaker.session')
            session['logged_in'] = True
            session['user_id'] = user['id_pessoa']
            session['user_name'] = user['nome']
            session['user_email'] = user['email']
            session.save()

            return {'success': True}

        except Exception as e:
            print(f"Erro no login: {e}")
            return {'success': False, 'errors': {'internal': 'Erro inesperado. Tente novamente.'}}

    def save(self, db):
        name = request.forms.get('nome')
        email = request.forms.get('email')
        cpf = request.forms.get('cpf')
        situacao = "A"
        senha = request.forms.get('senha')
        confirmarSenha = request.forms.get('confirmarSenha')
        
        errors = {}

        errors.update(self.validate_fields(email, senha))
        
        if senha != confirmarSenha:
            errors['confirmarSenha'] = 'As senhas não coincidem!' 

        exists = self.pessoa_model.get_by_email(db, email)
        if exists:
            errors['email'] = 'Email já cadastrado!' 

        if errors:
            return {'success': False, 'error': errors} 
        
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        pessoa = Pessoas(name=name, email=email, cpf=cpf, situacao=situacao, senha=senha_hash)
        novo_id = self.pessoa_model.add_pessoa(db, pessoa)
        
        if novo_id is None:
             return {'success': False, 'error': {'geral': 'Erro ao salvar no banco de dados.'}}

        return {'success': True, 'id': novo_id}

    def delete_user(self, db, pessoa_id):
        self.pessoa_model.delete_user(db, pessoa_id)
        return {'success': True}
