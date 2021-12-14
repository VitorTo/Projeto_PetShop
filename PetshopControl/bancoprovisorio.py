#importando módulo do SQlite
import sqlite3

class Petshop():
    def __init__(self):
        self.conexao = sqlite3.connect('petshop.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists cliente (
                     id integer primary key autoincrement ,
                     nome text,
	                 email text,		
                     telefone text,
                     endereco text,
                     cpf text)""")
        self.conexao.commit()   # verificar
        c.close()
