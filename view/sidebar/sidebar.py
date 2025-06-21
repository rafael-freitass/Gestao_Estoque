from controller.Controller import Controller
import tkinter as tk
import tkinter.messagebox as messagebox

class Sidebar(tk.Frame):
    def __init__(self, parent, controller_view):
        super().__init__(parent)
        self.controller_view = controller_view
        self.controller = controller_view.controller

        self.pack(fill="y")

        self.botao_estoque = tk.Button(self, text="Estoque", bg="#34495e", fg="white",
                  command=lambda: self.controller_view.show_frame("Tela_estoque")).pack(fill="x")

        self.botao_editar = tk.Button(self, text="Editar Produto", bg="#34495e", fg="white",
                  command=lambda: self.controller_view.show_frame("Tela_editar")).pack(fill="x")

        self.botao_registrar = tk.Button(self, text="Registrar Produto", bg="#34495e", fg="white",
                  command=lambda: self.controller_view.show_frame("Tela_registrar")).pack(fill="x")

        self.botao_sair = tk.Button(self, text="Sair", bg="#e74c3c", fg="white", command=self.exit).pack(fill="x")

    def exit(self):
        self.controller_view.root.destroy()
        return
        