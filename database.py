import sqlite3

class DataBase():
    def __init__(self, name = "registro.db") -> None:
        self.name = name
    
    def conecta(self):
        self.connection = sqlite3.connect(self.name)
    
    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def table_alunos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                    CREATE TABLE IF NOT EXISTS alunos(
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        idade INT TEXT NOT NULL,
                        genero TEXT NOT NULL
                    );
            
            """)
        except AttributeError:
            print("faça a conexão")
        self.close_connection()

    def ver_tabela(self):

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT * FROM alunos
            
            """)
            self.result = cursor.fetchall()
            return self.result
        except AttributeError:
            print("faça a conexão")
    
    def filtro(self, nome, genero):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                SELECT * FROM alunos WHERE nome = ? or genero = ?
            
            """,(nome, genero))
            self.all = cursor.fetchall()
            return self.all
        except AttributeError:
            print("Falha na conexão")

    def cadastrar(self, nome, idade, genero):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO alunos (nome, idade, genero) VALUES (?,?,?)
            
            """,(nome, idade, genero))
            self.connection.commit()
        except AttributeError:
            print("Falha na conexão")

if __name__=="__main__":
    db = DataBase()
    db.conecta()
    db.table_alunos()
    db.close_connection()