from view.tabela.Tabela_produtos import Tabela_produtos
from view.edicao.Formulario_edicao import Formulario_edicao
import tkinter as tk

class Tela_editar(tk.Frame):
    def __init__(self, frame_pai, instancia_view):
        super().__init__(frame_pai, bg="#ffffff")
        self.controller = instancia_view.controller
        self.rowconfigure(2, weight=1)

        self.titulo = tk.Label(self, text="EDITAR PRODUTOS", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        self.frame_tabela = tk.Frame(self, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0, sticky="nsew")

        self.frame_editar_produto = tk.Frame(self, bg="#ffffff")
        self.frame_editar_produto.grid(row=1, column=0, sticky="nsew")
        
        self.tabela = Tabela_produtos(self.frame_tabela, self.controller, tipo_tabela="editar", callback_botao_editar=self.mostrar_formulario_edicao)
        self.tabela.grid(row=2, column=0)

        self.frame_tabela.tkraise()

    def mostrar_formulario_edicao(self, produto_id):
        for widget in self.frame_editar_produto.winfo_children():
            widget.destroy()

        formulario_edicao = Formulario_edicao(self.frame_editar_produto, self.controller, produto_id, callback_botao_voltar=self.voltar_para_tabela)
        formulario_edicao.grid(row=2, column=0)
        
        self.frame_editar_produto.tkraise()

    def voltar_para_tabela(self):
        self.tabela.atualizar_tabela()
        self.frame_tabela.tkraise()
