from typing import Dict
from model.Model import Model

class Controller:
    def __init__(self, view):
        self.view = view
        self.model = Model()
    
    def handle_exit(self):
        self.view.root.destroy()
        return

    def abrir_tela_estoque(self):
        self.view.show_frame("Tela_estoque")

    def abrir_tela_editar(self):
        self.view.show_frame("Tela_editar")
    
    def abrir_tela_registrar(self):
        self.view.show_frame("Tela_registrar")

    def produtos_em_estoque(self):
        return self.model.produtos_em_estoque()

    def buscar_produto(self, id):
        return self.model.buscar_produto(id)

    def registrar_produto(self, valores:Dict):
        return self.model.registrar_produto(valores)
    
    def registrar_entrada(self, id):
        return self.model.registro_entrada(id)

    def registrar_saida(self, id):
        return self.model.registro_saida(id)

    def atualizar_produto(self, id, dados: dict):
        return self.model.atualizar_produto(id, dados)

    def excluir_produto(self, id):
        self.model.excluir_produto(id)

    def buscar_quantidade(self, produto_id):
        return self.model.buscar_quantidade_produto(produto_id)
    
    def data_hoje(self):
        return self.model.data_hoje()
    
    def calcular_total_saidas(self):
        return self.model.calcular_total_saidas()