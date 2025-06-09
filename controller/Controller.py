from typing import Dict
from model.Model import Model

class Controller:
    def __init__(self):
        self.model = Model()
    
    def produtos_em_estoque(self):
        return self.model.produtos_em_estoque()

    def registrar_produto(self, valores:Dict):
        self.model.registrar_produto(valores)
    
    def registrar_entrada(self):
        self.model.registro_entrada(self)

    def registrar_saida(self):
        self.model.registro_saida(self)