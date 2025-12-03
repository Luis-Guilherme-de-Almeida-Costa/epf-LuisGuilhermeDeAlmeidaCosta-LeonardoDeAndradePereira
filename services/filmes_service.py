from models.filmes import FilmesModel, Filmes
from typing import Dict, Any, Optional
from datetime import datetime
import os
from utils.validate import ValidateFields
from validators import length, ValidationError 


class FilmesService:
    def __init__(self):

        self.filmes_model = FilmesModel() 
        self.validate_fields = ValidateFields()

    def get_all(self, db) -> list:
        try:
            return self.filmes_model.get_all(db)
        except Exception as e:
            print(f"Erro no Service ao buscar todos os filmes: {e}")
            return []

    def get_by_id(self, db, filme_id: int) -> Optional[Dict[str, Any]]:
        try:
            return self.filmes_model.get_by_id(db, filme_id)
        except Exception as e:
            print(f"Erro no Service ao buscar filme por ID {filme_id}: {e}")
            return None

    def get_by_category(self, db, category):
        return self.filmes_model.get_by_category(db, category)

    def get_by_name(self, db, title):
        return self.filmes_model.get_by_name(db, title)

    def add_filme(self, db, filme_data):

        self.validate_fields.verificaTitulo(filme_data.get('titulo', ''))
        self.validate_fields.verificaCategoria(filme_data.get('categoria', ''))
        self.validate_fields.verificaDiretor(filme_data.get('diretor', ''))
        self.validate_fields.verificaSinopse(filme_data.get('sinopse', ''))

        errors = self.validate_fields.errors

        if errors:
                errors_to_return = errors
                self.validate_fields.errors = {}
                return {'success': False, 'errors': errors_to_return}
        
        filme_entity = Filmes(
            titulo=filme_data.get('titulo', ''),
            categoria=filme_data.get('categoria', ''),
            sinopse=filme_data.get('sinopse', ''),
            diretor=filme_data.get('diretor', ''),
            capa_path=filme_data.get('capa_path', ''),
            video_path=filme_data.get('video_path', ''),
            id_administrador=filme_data.get('id_administrador'),
            data_exibicao=filme_data.get('data_exibicao'), 
            status=filme_data.get('status')
        )

        try:
            novo_id = self.filmes_model.insert_filme(db, filme_entity)
            
            return {'success': True, novo_id: novo_id}

        except Exception as e:
            print(f"Erro no Service ao adicionar filme no banco: {e}")
            return {
                'success': False, 
                'errors': {'geral': 'Erro interno ao salvar no banco de dados. Verifique o log do servidor.'}
            }

    def delete_filme(self, db, filme_id):
        try:
            linhas_deletadas, capa_path, video_path = self.filmes_model.delete_filme(db, filme_id)
        
            self._remove_file(capa_path)
            self._remove_file(video_path)

            return {'success': True}
        except Exception as e:
            print(f"Erro no Service ao deletar filme ID {filme_id} do BD: {e}")
            return False

    def _remove_file(self, file_path: Optional[str]):
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Aviso: Não foi possível remover o arquivo {file_path}. Erro: {e}")