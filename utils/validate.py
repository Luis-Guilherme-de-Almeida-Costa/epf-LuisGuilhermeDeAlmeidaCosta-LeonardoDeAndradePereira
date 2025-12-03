from validators import email as validate_email, length, ValidationError
import re

class ValidateFields:
    def __init__(self):
        self.errors = {}

    def verificarEmail(self, email):
        if not email:
            self.errors['email'] = "O campo email não pode ficar vazio!"
            return
        
        try:
            if not validate_email(email):
                self.errors['email'] = "Email inválido."
                return
        except ValidationError:
            self.errors['email'] = "Email em formato inválido."

    def verificarSenha(self, senha):
        if not senha:
            self.errors['senha'] = "O campo senha não pode ficar vazio!"
            return
            
        tamanho = len(senha)
        if tamanho < 6 or tamanho > 255:
            self.errors['senha'] = "A senha deve ter entre 6 e 255 caracteres."
            return

    def verificarNome(self, nome):
        if not nome:
            self.errors['nome'] = "O campo nome não pode ficar vazio!"
            return

        tamanho = len(nome)
        if tamanho < 3 or tamanho > 55:
            self.errors['nome'] = "O nome deve ter entre 3 e 55 caracteres."
            return

    def verificaCpf(self, cpf):
        if not cpf:
            self.errors['cpf'] = "O campo CPF não pode ficar vazio!"
            return
        
        cpf_limpo = re.sub(r'[^\d]', '', cpf)
        
        if len(cpf_limpo) != 11:
            self.errors['cpf'] = "O CPF deve conter exatamente 11 dígitos numéricos."
            return

    def verificaTitulo(self, titulo):
        if not titulo:
            self.errors['titulo'] = "O campo título não pode ficar vazio!"
            return
            
        tamanho = len(titulo)
        if tamanho < 6 or tamanho > 255:
            self.errors['titulo'] = "O título deve ter entre 6 e 255 caracteres."
            return
        
    def verificaCategoria(self, categoria):
        if not categoria:
            self.errors['categoria'] = "O campo categoria não pode ficar vazio!"
            return
            
        tamanho = len(categoria)
        
        if tamanho < 6 or tamanho > 255:
            self.errors['categoria'] = "A categoria deve ter entre 6 e 255 caracteres."
            return
    
    def verificaDiretor(self, diretor):
        if not diretor:
            self.errors['diretor'] = "O campo diretor não pode ficar vazio!"
            return
            
        tamanho = len(diretor)
        if tamanho < 6 or tamanho > 50:
            self.errors['diretor'] = "O diretor deve ter entre 6 e 50 caracteres."
            return
    
    def verificaSinopse(self, sinopse):
        if not sinopse:
            self.errors['sinopse'] = "O campo sinopse não pode ficar vazio!"
            return
            
        tamanho = len(sinopse)
        if tamanho < 6 or tamanho > 500:
            self.errors['sinopse'] = "A sinopse deve ter entre 6 e 500 caracteres."
            return