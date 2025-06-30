from controller.Controller import Controller
import tkinter as tk

from view.estoque.Tela_estoque import Tela_estoque
from view.edicao.Tela_editar import Tela_editar
from view.registro.Tela_registrar import Tela_registrar
from view.sidebar.sidebar import Sidebar

class View:
    def __init__(self):
        self.controller = Controller(self)
        
        self.root = tk.Tk()
        self.root.title("Gestão de Estoque")
        self.root.geometry("1000x600")

        self.sideContainer = tk.Frame(self.root, width=100, height=600, bg="#ffffff")
        self.sideContainer.pack(side="left", fill="y", padx=5, pady=10)

        self.mainContainer = tk.Frame(self.root, bg="#ffffff")
        self.mainContainer.pack(side="right", fill="both", expand=True, padx=5, pady=10)

        self.sidebar = Sidebar(self.sideContainer, self)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.tela_estoque = Tela_estoque(self.mainContainer, self)
        self.tela_estoque.grid(row=0, column=0, sticky="nsew")

        self.tela_editar = Tela_editar(self.mainContainer, self)
        self.tela_editar.grid(row=0, column=0, sticky="nsew")

        self.tela_registrar = Tela_registrar(self.mainContainer, self)
        self.tela_registrar.grid(row=0, column=0, sticky="nsew")

        self.frames = {
            "Tela_estoque": self.tela_estoque,
            "Tela_editar": self.tela_editar,
            "Tela_registrar": self.tela_registrar
        }
        self.show_frame("Tela_estoque")

        self.root.mainloop()

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        
        if hasattr(frame, "tabela"):
            frame.tabela.atualizar_tabela()

        frame.tkraise()