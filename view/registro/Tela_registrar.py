import tkinter as tk

class Tela_registrar(tk.Frame):
    def __init__(self, frame_pai, instancia_view):
        super().__init__(frame_pai, bg="#ffffff")

        self.controller = instancia_view.controller
        
        self.rowconfigure(2, weight=0)

        self.titulo = tk.Label(self, text="Registar Produto", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        self.nome = tk.Label(self, text="Nome:", bg="#ffffff")
        self.nome.grid(row=1, column=0)
        self.inserir_nome = tk.Entry(self, width=20, validate="key")
        self.inserir_nome.grid(row=1, column=1)

        self.categoria = tk.Label(self, text="Categoria:", bg="#ffffff")
        self.categoria.grid(row=2, column=0)
        self.inserir_categoria = tk.Entry(self, width=20, validate="key")
        self.inserir_categoria.grid(row=2, column=1)

        self.quantidade = tk.Label(self, text="Quantidade:", bg="#ffffff")
        self.quantidade.grid(row=3, column=0)
        self.inserir_quantidade = tk.Entry(self, width=20, validate="key")
        self.inserir_quantidade.grid(row=3, column=1)

        self.preco = tk.Label(self, text="Preco:", bg="#ffffff")
        self.preco.grid(row=4, column=0)
        self.inserir_preco = tk.Entry(self, width=20, validate="key")
        self.inserir_preco.grid(row=4, column=1)

        self.frame_botoes = tk.Frame(self, bg="#ffffff")
        self.frame_botoes.grid(row=5, column=1, columnspan=2)
        
        self.botao_limpar = tk.Button(self.frame_botoes, text='Limpar', command= lambda: self.limpar_entry())
        self.botao_limpar.grid(row=0, column=0, padx= 5)

        self.botao_salvar = tk.Button(self.frame_botoes, text='Salvar', command= lambda: self.salvar_e_voltar())
        self.botao_salvar.grid(row=0, column=1, padx= 5)

    def salvar_e_voltar(self):
        self.controller.registrar_produto(self.pegar_dados())
        self.controller.abrir_tela_estoque()

    def limpar_entry(self):
        self.inserir_nome.delete(0, tk.END)
        self.inserir_categoria.delete(0, tk.END),
        self.inserir_quantidade.delete(0, tk.END),
        self.inserir_preco.delete(0, tk.END)

    def pegar_dados(self):
        return {
        "nome" : self.inserir_nome.get(),
        "categoria" : self.inserir_categoria.get(),
        "quantidade" : self.inserir_quantidade.get(),
        "preco" : self.inserir_preco.get()
        }