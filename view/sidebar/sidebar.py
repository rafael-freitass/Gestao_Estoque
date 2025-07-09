import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, frame_pai, instancia_view):
        super().__init__(frame_pai, bg="#ffffff")
        
        self.controller = instancia_view.controller
        
        self.montar_sidebar()

    def montar_sidebar(self):
        container = self

        self.botao_estoque = tk.Button(container, text="Estoque", bg="#34495e", fg="white",
                  command=lambda: self.controller.abrir_tela_estoque())
        self.botao_estoque.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)

        self.botao_editar = tk.Button(container, text="Editar Produto", bg="#34495e", fg="white",
                  command=lambda: self.controller.abrir_tela_editar())
        self.botao_editar.grid(row=1, column=0, sticky="nsew", pady=5, padx=5)

        self.botao_registrar = tk.Button(container, text="Registrar Produto", bg="#34495e", fg="white",
                  command=lambda: self.controller.abrir_tela_registrar())
        self.botao_registrar.grid(row=2, column=0, sticky="nsew", pady=5, padx=5)

        self.botao_sair = tk.Button(container, text="Sair", bg="#e74c3c", fg="white", command=self.exit)
        self.botao_sair.grid(row=3, column=0, sticky="nsew", pady=5, padx=5)


    def exit(self):
        self.controller.handle_exit()
        