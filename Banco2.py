#importando módulo do SQlite
import sqlite3

class Banco():

    def __init__(self):
        self.veriferro = sqlite3
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists controles (
                     idcont integer primary key autoincrement,
                     tipo text,
                     historico text,
                     compet integer,
                     ccusto text,
                     doc text,
                     valor integer,
                     vcto date,
                     pgto date,
                     fpg text,
                     status text,
                     saldo integer)""")
        self.conexao.commit()
        c.close()
