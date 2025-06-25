from datetime import datetime

from model.DatabaseSQLite import Database_SQLite
from model.DatabaseCSV import Database_CSV

class Model:
    def __init__(self):
        self.db_sqlite = Database_SQLite()
        self.db_csv = Database_CSV()
    
    def registrar_produto(self, valores):
        self.db_sqlite.registrar_produto(valores)

    def registro_entrada(self, id):
        produto = self.db_sqlite.buscar_produto(id)
        self.db_sqlite.registrar_entrada(id)
        self.db_csv.registrar_entrada(produto[1], 1, produto[4])

    def registro_saida(self, id):
        produto = self.db_sqlite.buscar_produto(id)
        if produto and produto[3] > 0:
            self.db_sqlite.registrar_saida(id)
            self.db_csv.registrar_saida(produto[1], 1, produto[4])
            return True
        else:
            return False

    def buscar_produto(self, id):
        return self.db_sqlite.buscar_produto(id)

    def produtos_em_estoque(self):
        return self.db_sqlite.listar_produtos_estoque()

    def vendas_dia(self):
        pass

    def atualizar_produto(self, id, dados):
        self.db_sqlite.atualizar_produto(id, dados)

    def excluir_produto(self, id):
        self.db_sqlite.excluir_produto(id)

    def buscar_quantidade_produto(self, produto_id):
        return self.db_sqlite.buscar_quantidade_produto(produto_id)
    
    def data_hoje(self):
        data = datetime.now().strftime("%d/%m/%Y")
        return data

    def calcular_total_saidas(self):
        return self.db_csv.calcular_total_saidas()