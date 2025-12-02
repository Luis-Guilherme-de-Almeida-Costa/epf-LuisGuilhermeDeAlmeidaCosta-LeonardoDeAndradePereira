from bottle import request, redirect
from models.pessoas import PessoasModel, Pessoas
import bcrypt
from validators import email as validate_email, length, ValidationError
class PessoasService:
    def __init__(self):
        self.pessoa_model = PessoasModel()

    def get_all(self, db):
        return self.pessoa_model.get_all(db)
    
    def get_by_id(self, db, pessoa_id):
        return self.pessoa_model.get_by_id(db, pessoa_id)

    def get_administrador_by_id(self, db, pessoa_id):
        return self.pessoa_model.get_administrador_by_id(db, pessoa_id)
    
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
    
    def edit(self, db, pessoa_id):
        try:
            nome = request.forms.get('nome', '').strip()
            email = request.forms.get('email', '').strip()
            cpf = request.forms.get('cpf', '').strip()
            

            current_data = {
                'nome': nome,
                'email': email,
                'cpf': cpf
            }

            errors = {}

            if not nome:
                errors['nome'] = "O nome não pode estar vazio."
            if not email:
                errors['email'] = "O email não pode estar vazio."
            if not cpf:
                errors['cpf'] = "O CPF não pode estar vazio."

            existing = self.pessoa_model.get_by_email(db, email)
            
            if existing and existing['id_pessoa'] != pessoa_id:
                errors['email'] = "Este email já está cadastrado em outra conta."

            if errors:
                return {
                    "success": False,
                    "errors": errors,
                    "data": current_data
                }

            pessoa = self.pessoa_model.get_by_id(db, pessoa_id)
            if not pessoa:
                return {
                    "success": False,
                    "errors": {"geral": "Usuário não encontrado."},
                    "data": current_data
                }

            pessoa['nome'] = nome
            pessoa['email'] = email
            pessoa['cpf'] = cpf

            ok = self.pessoa_model.update_pessoa(db, pessoa, pessoa_id)

            if not ok:
                return {
                    "success": False,
                    "errors": {"geral": "Erro ao atualizar usuário no banco de dados."},
                    "data": current_data
                }

            return {
                "success": {"Sucesso": "Dados atualizados com sucesso!"},
            }

        except Exception as e:
            print("ERRO EDIT SERVICE:", e)
            return {
                "success": False,
                "errors": {"geral": "Erro interno ao tentar atualizar o usuário."},
                "data": current_data
            }


    def logout(self):
        session = request.environ.get('beaker.session')
        session.delete()
