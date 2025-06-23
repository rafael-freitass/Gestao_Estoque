from typing import Dict
from model.Model import Model

class Controller:
    def __init__(self):
        self.model = Model()
    
    def produtos_em_estoque(self):
        return self.model.produtos_em_estoque()

    def buscar_produto(self, id):
        return self.model.buscar_produto(id)

    def registrar_produto(self, valores:Dict):
        self.model.registrar_produto(valores)
    
    def registrar_entrada(self, id):
        self.model.registro_entrada(id)

    def registrar_saida(self, id):
        self.model.registro_saida(id)

    def atualizar_produto(self, id, dados: dict):
        self.model.atualizar_produto(id, dados)

    def excluir_produto(self, id):
        self.model.excluir_produto(id)

    def buscar_quantidade(self, produto_id):
        return self.model.buscar_quantidade_produto(produto_id)