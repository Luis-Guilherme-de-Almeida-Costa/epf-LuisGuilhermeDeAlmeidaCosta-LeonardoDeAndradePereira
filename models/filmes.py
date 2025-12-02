from datetime import datetime
from typing import Optional

# Classe de Entidade/Objeto de Dados para um Filme
class FilmesModel:
    def __init__(self, 
                 titulo: str, 
                 categoria: str, 
                 capa_path: str, 
                 video_path: str, 
                 id_usuario: int,
                 data_exibicao: Optional[datetime] = None, 
                 status: str = 'ATIVO',
                 id: Optional[int] = None,
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None):
        """
        Inicializa o objeto Filme.
        
        data_exibicao: Deve ser um objeto datetime.datetime ou None.
        status: 'ATIVO' ou 'AGENDADO'.
        """
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.data_exibicao = data_exibicao
        self.status = status
        self.capa_path = capa_path
        self.video_path = video_path
        self.id_usuario = id_usuario
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Filme {self.titulo} (ID: {self.id or 'Novo'}) - Status: {self.status}>"

    def to_dict(self):
        """Converte o objeto Filme para um dicionário."""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'categoria': self.categoria,
            'data_exibicao': self.data_exibicao,
            'status': self.status,
            'capa_path': self.capa_path,
            'video_path': self.video_path,
            'id_usuario': self.id_usuario,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


# Classe de Interação com o Banco de Dados (CRUD)
class FilmesModel:
    
    def __init__(self):
        self.table_name = 'filmes'

    def insert_filme(self, db, filme: Filmes):
        """
        Insere um novo filme no banco de dados.

        :param db: Conexão ativa com o banco de dados.
        :param filme: Objeto Filmes com os dados a serem inseridos.
        :return: ID do filme inserido ou None em caso de erro.
        """
        try:
            cursor = db.cursor()
            sql = f"""
                INSERT INTO {self.table_name} 
                (titulo, categoria, data_exibicao, status, capa_path, video_path, id_usuario) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            
            # Formata a data de exibição para o formato SQL, se existir
            data_exibicao_db = filme.data_exibicao.strftime('%Y-%m-%d %H:%M:%S') if filme.data_exibicao else None

            cursor.execute(sql, (
                filme.titulo,
                filme.categoria,
                data_exibicao_db,
                filme.status,
                filme.capa_path,
                filme.video_path,
                filme.id_usuario
            ))
            
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print(f"Erro ao inserir novo filme: {e}")
            return None

    def get_all(self, db):
        """Busca todos os filmes no banco de dados."""
        try:
            cursor = db.cursor(dictionary=True)
            # Seleciona todos os campos, incluindo os caminhos dos arquivos
            cursor.execute(f"SELECT * FROM {self.table_name}")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar filmes: {e}")
            return []

    def get_by_id(self, db, filme_id):
        """Busca um filme pelo seu ID."""
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE id = %s", (filme_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar filme com ID {filme_id}: {e}")
            return None