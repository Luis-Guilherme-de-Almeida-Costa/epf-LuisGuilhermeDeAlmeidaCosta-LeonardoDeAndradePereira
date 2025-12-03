from datetime import datetime
from typing import Optional

# Classe de Entidade/Objeto de Dados para um Filme
class Filmes:
    def __init__(self, 
                 titulo: str, 
                 categoria: str, 
                 sinopse: str,
                 diretor: str,
                 capa_path: str, 
                 video_path: str, 
                 id_administrador: int,
                 data_exibicao: Optional[datetime] = None, 
                 status: str = 'ATIVO',
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None):
    
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.sinopse = sinopse 
        self.diretor = diretor
        self.data_exibicao = data_exibicao
        self.status = status
        self.capa_path = capa_path
        self.video_path = video_path
        self.id_administrador = id_administrador
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Filme {self.titulo} (ID: {self.id or 'Novo'}) - Status: {self.status}>"

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'categoria': self.categoria,
            'data_exibicao': self.data_exibicao,
            'status': self.status,
            'capa_path': self.capa_path,
            'video_path': self.video_path,
            'id_administrador': self.id_administrador,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class FilmesModel:
    
    def __init__(self):
        self.table_name = 'filmes'

    def delete_filme(self, db, filme_id):
        filme_data = self.get_by_id(db, filme_id)
        try:
            cursor = db.cursor()
            sql = f"DELETE FROM {self.table_name} WHERE id_filmes = %s"
            
            cursor.execute(sql, (filme_id,))
            db.commit()
            return (cursor.rowcount, filme_data['capa_path'], filme_data['video_path']) 
        except Exception as e:
            db.rollback()
            print(f"Erro ao deletar filme com ID {filme_id}: {e}")
            return 0

    def insert_filme(self, db, filme: Filmes):
   
        try:
            cursor = db.cursor()
            sql = f"""
                INSERT INTO {self.table_name} 
                (titulo, categoria, sinopse, diretor, data_exibicao, status, capa_path, video_path, id_administrador) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            data_exibicao_db = filme.data_exibicao.strftime('%Y-%m-%d %H:%M:%S') if filme.data_exibicao else None
            
            cursor.execute(sql, (
                filme.titulo,
                filme.categoria,
                filme.sinopse,
                filme.diretor,
                data_exibicao_db,
                filme.status,
                filme.capa_path,
                filme.video_path,
                filme.id_administrador
            ))
            
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print(f"Erro ao inserir novo filme: {e}")
            return e

    def get_all(self, db):
        try:
            cursor = db.cursor(dictionary=True)
          
            cursor.execute(f"SELECT * FROM {self.table_name}")
            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar filmes: {e}")
            return []

    def get_by_category(self, db, category):
        try:
            cursor = db.cursor(dictionary=True)
            
            sql = f"SELECT * FROM {self.table_name} WHERE categoria LIKE %s"
            
            search_term = f"%{category}%"
        
            cursor.execute(sql, (search_term,))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Erro ao buscar filmes da categoria '{category}': {e}")
            return []
        
    def get_by_name(self, db, title):
        try:
            cursor = db.cursor(dictionary=True)
            
            sql = f"SELECT * FROM {self.table_name} WHERE titulo LIKE %s"
            
            search_term = f"%{title}%"
        
            cursor.execute(sql, (search_term,))
            
            return cursor.fetchall()
            
        except Exception as e:
            print(f"Erro ao buscar filmes da categoria '{category}': {e}")
            return []
        
    def get_by_id(self, db, filme_id):
        try:
            cursor = db.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {self.table_name} WHERE id_filmes = %s", (filme_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar filme com ID {filme_id}: {e}")
            return None