import model.database as database

class Model:
    def __init__(self):
        self.database = database
    
    def registrar_produto(self, valores):
        self.database.registrar_produto(valores)

    def registro_entrada(self, id):
        self.database.registrar_entrada(id)

    def registro_saida(self, id):
        self.database.registrar_saida(id)

    def buscar_produto(self, id):
        return database.buscar_produto(id)

    def produtos_em_estoque(self):
        return self.database.listar_produtos_estoque()

    def vendas_dia(self):
        pass

    def atualizar_produto(self, id, dados):
        self.database.atualizar_produto(id, dados)

    def excluir_produto(self, id):
        self.database.excluir_produto(id)

    def buscar_quantidade_produto(self, produto_id):
        return self.database.buscar_quantidade_produto(produto_id)