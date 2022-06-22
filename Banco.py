import sqlite3


class Banco():


    
    def __init__(self):
        self.conexao = sqlite3.connect('participante.db')
        self.createTable()


    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists participante(
                     id integer primary key autoincrement,
                     nome text,
                     login text,
                     senha text,
                     email text,
                     endereco text,
                     telefone text)""")
        self.conexao.commit()
        c.close()