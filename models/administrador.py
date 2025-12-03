class AdministradorModel:
    
    def get_all(self, db):
        try:
            cursor = db.cursor(dictionary=True)
            sql_query = """
                SELECT 
                    a.id_administrador, 
                    p.*
                FROM 
                    administrador a
                INNER JOIN 
                    pessoas p ON a.id_pessoa = p.id_pessoa
            """

            cursor.execute(sql_query)

            return cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar pessoas: {e}")
            return []

    def add_administrador(self, db, id_pessoa):
        try:
            cursor = db.cursor()
            sql = """
                INSERT INTO administrador (id_pessoa)
                VALUES (%s)
            """
            cursor.execute(sql, (id_pessoa,))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print(f"Erro ao inserir nova pessoa: {e}")
            return None