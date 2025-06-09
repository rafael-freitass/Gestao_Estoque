import model.database as database

class Model:
    def __init__(self):
        pass
    
    def registrar_produto(self, valores):
        database.registrar_produto(valores)

    def registro_entrada(self, id):
        database.registrar_entrada(id)

    def registro_saida(self, id):
        database.registrar_saida(id)

    def produtos_em_estoque(self):
        return database.listar_produtos_estoque()

    def vendas_dia(self):
        pass