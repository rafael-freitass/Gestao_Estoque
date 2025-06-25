import tkinter as tk
from view.tabela.Tabela_produtos import Tabela_produtos

class Tela_estoque(tk.Frame):
    def __init__(self, frame_pai, instancia_view):
        super().__init__(frame_pai, bg="#ffffff")

        self.controller = instancia_view.controller
        self.data = self.controller.data_hoje()
        self.vendas_dia = self.controller.calcular_total_saidas()
        

        # título da tela
        self.titulo = tk.Label(self, text="ESTOQUE", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        # frame da tabela de produtos
        self.frame_tabela = tk.Frame(self, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)

        # chama a tabela de estoque
        self.tabela = Tabela_produtos(self.frame_tabela, self.controller, tipo_tabela="estoque", callback_atualizar_vendas=self.atualizar_vendas)
        self.tabela.grid(row=2, column=0)

        # texto para qtd de vendas no dia
        self.info_vendas = tk.Label(self, text=f"Vendas do dia {self.data}: R${self.vendas_dia:.2f}", font=("Arial", 20), bg="#ffffff")
        self.info_vendas.grid(row=3, column=0)
    
    def atualizar_vendas(self):
        self.nova_venda = self.controller.calcular_total_saidas()
        self.info_vendas.config(text=f"Vendas do dia {self.data}: R${self.nova_venda:.2f}")