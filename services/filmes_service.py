from models.filmes import FilmesModel, Filmes
from typing import Dict, Any, Optional
from datetime import datetime
import os

from validators import length, ValidationError 


class FilmesService:
    def __init__(self):

        self.filmes_model = FilmesModel() 

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

    def validate_filme_data(self, titulo: str, categoria: str, diretor: str, sinopse: str) -> Dict[str, str]:
        errors = {}

        if not titulo or len(titulo.strip()) < 3:
            errors['titulo'] = "O título é obrigatório e deve ter no mínimo 3 caracteres."
            
        if not categoria or categoria == 'Selecione uma categoria':
            errors['categoria'] = "A categoria é obrigatória."
            
        if not diretor or len(diretor.strip()) < 3:
            errors['diretor'] = "O nome do diretor é obrigatório."

        if not sinopse or len(sinopse.strip()) < 10:
             errors['sinopse'] = "A sinopse é obrigatória e deve ter no mínimo 10 caracteres."
        
        try:
            length(sinopse, max=500)
        except ValidationError:
             errors['sinopse'] = "A sinopse não pode exceder 500 caracteres."
             
        return errors

    def add_filme(self, db, filme_data):
        errors = self.validate_filme_data(filme_data.get('titulo', ''),filme_data.get('categoria', ''), filme_data.get('diretor', ''), filme_data.get('sinopse', ''))

        if errors:
                return {'success': False, 'errors': errors}
        
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

    def delete_filme(self, db, filme_id: int, capa_path: str, video_path: str) -> bool:
        try:
            ok = self.filmes_model.delete_filme(db, filme_id)
        except Exception as e:
            print(f"Erro no Service ao deletar filme ID {filme_id} do BD: {e}")
            return False
        
        if ok:
            self._remove_file(capa_path)
            self._remove_file(video_path)
            
        return ok

    def _remove_file(self, file_path: Optional[str]):
        if file_path and os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Aviso: Não foi possível remover o arquivo {file_path}. Erro: {e}")