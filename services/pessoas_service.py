from bottle import request, redirect
from models.pessoas import PessoasModel, Pessoas
from utils.validate import ValidateFields
import bcrypt
class PessoasService:
    def __init__(self):
        self.pessoa_model = PessoasModel()
        self.validate_fields = ValidateFields()

    def get_all(self, db):
        return self.pessoa_model.get_all(db)
    
    def get_by_id(self, db, pessoa_id):
        return self.pessoa_model.get_by_id(db, pessoa_id)

    def get_administrador_by_id(self, db, pessoa_id):
        return self.pessoa_model.get_administrador_by_id(db, pessoa_id)

    def login(self, db):
        try:
            email = request.forms.get('email')
            senha = request.forms.get('senha')

            self.validate_fields.verificarEmail(email)
            self.validate_fields.verificarSenha(senha)

            errors = self.validate_fields.errors
            
            if errors:
                errors_to_return = errors
                self.validate_fields.errors = {}
                return {'success': False, 'errors': errors_to_return}

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
        
        self.validate_fields.verificarNome(name)
        self.validate_fields.verificarEmail(email)
        self.validate_fields.verificarSenha(senha)
        self.validate_fields.verificaCpf(cpf)

        verificaCpfRepetido = self.pessoa_model.get_all(db)

        errors = self.validate_fields.errors
        for i in verificaCpfRepetido:     
            if(i['cpf'] == cpf):
                errors['CpfRepetido'] = "Esse cpf já foi utilizado!"

        if senha != confirmarSenha:
            errors['confirmarSenha'] = 'As senhas não coincidem!' 

        exists = self.pessoa_model.get_by_email(db, email)
        if exists:
            errors['email'] = 'Email já cadastrado!' 

        if errors:
            errors_to_return = errors
            self.validate_fields.errors = {}
            return {'success': False, 'error': errors_to_return} 
        
        senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        pessoa = Pessoas(name=name, email=email, cpf=cpf, situacao=situacao, senha=senha_hash)
        novo_id = self.pessoa_model.add_pessoa(db, pessoa)
        
        if novo_id is None:
             return {'success': False, 'error': {'geral': 'Erro ao salvar no banco de dados.'}}

        return {'success': True, 'id': novo_id}
    
    def edit(self, db, pessoa_id, cpf_user):
        try:

            nome = request.forms.get('nome', '').strip()
            email = request.forms.get('email', '').strip()
            cpf = request.forms.get('cpf', '').strip()

            current_data = {
                'nome': nome,
                'email': email,
                'cpf': cpf
            }

            self.validate_fields.verificarNome(nome)
            self.validate_fields.verificarEmail(email)
            self.validate_fields.verificaCpf(cpf)
            verificaCpfRepetido = self.pessoa_model.get_all(db)            

            errors = self.validate_fields.errors
            for i in verificaCpfRepetido:
                if(i['cpf'] == cpf and i['cpf'] != cpf_user):
                    errors['CpfRepetido'] = "Esse cpf já foi utilizado!"

            existing = self.pessoa_model.get_by_email(db, email)
            
            if existing and existing['id_pessoa'] != pessoa_id:
                errors['email'] = "Este email já está cadastrado em outra conta."

            if errors:
                errors_to_return = errors
                self.validate_fields.errors = {}
                return { "success": False, "errors": errors_to_return, "data": current_data }

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
