class Pessoas:
    def __init__(self, name, email, cpf, situacao, senha):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.situacao = situacao
        self.senha = senha

    def __repr__(self):
        return f"<Pessoa {self.name} ({self.email})>"

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'cpf': self.cpf,
            'situacao': self.situacao,
            'senha': self.senha
        }


class PessoasModel:
    
    def get_all(self, db):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id_pessoa, name, email, cpf, situacao, senha_hash FROM pessoas")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar pessoas: {e}")
            return []

    
    def get_by_id(self, db, pessoa_id):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id_pessoa, nome, email, cpf, situacao, senha_hash FROM pessoas WHERE id_pessoa = %s", (pessoa_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar pessoa com ID {pessoa_id}: {e}")
            return None
    
    def get_by_email(self, db, email):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT id_pessoa, nome, email, cpf, situacao, senha_hash FROM pessoas WHERE email = %s", (email,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar pessoa com Email {email}: {e}")
            return None


    def add_pessoa(self, db, pessoa: Pessoas):
        try:
            cursor = db.cursor()
            sql = """
                INSERT INTO pessoas (nome, email, cpf, situacao, senha_hash)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (pessoa.name, pessoa.email, pessoa.cpf, pessoa.situacao, pessoa.senha))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print(f"Erro ao inserir nova pessoa: {e}")
            return None


    def update_pessoa(self, db, pessoa, id_pessoa):
        try:
            cursor = db.cursor()
            sql = """
                UPDATE pessoas
                SET nome = %s, email = %s, cpf = %s
                WHERE id_pessoa = %s
            """
            cursor.execute(sql, (pessoa['nome'], pessoa['email'], pessoa['cpf'], id_pessoa))
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao atualizar pessoa ID {id_pessoa}: {e}")
            return False


    def delete_pessoa(self, db, email):
        try:
            cursor = db.cursor()
            cursor.execute("DELETE FROM pessoas WHERE email = %s", (email,))
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao deletar pessoa EMAIL {email}: {e}")
            return False
