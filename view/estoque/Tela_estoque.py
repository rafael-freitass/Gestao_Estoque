import tkinter as tk
from view.tabela.Tabela_produtos import TabelaProdutos

class Tela_estoque(tk.Frame):
    def __init__(self, parent, controller_view):
        super().__init__(parent, bg="#ffffff")
        self.controller_view = controller_view
        self.controller = controller_view.controller

        # título da tela
        self.titulo = tk.Label(self, text="ESTOQUE", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        # frame da tabela de produtos
        self.frame_tabela = tk.Frame(self, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)

        # chama a tabela de estoque
        self.tabela = TabelaProdutos(self.frame_tabela, self.controller, tipo_tabela="estoque")
        self.tabela.grid(row=2, column=0)

        # texto para qtd de vendas no dia
        self.info_vendas = tk.Label(self, text="Vendas do dia:", font=("Arial", 20), bg="#ffffff")
        self.info_vendas.grid(row=3, column=0)
    