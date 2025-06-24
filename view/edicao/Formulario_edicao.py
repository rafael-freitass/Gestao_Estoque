import tkinter as tk

class Formulario_edicao(tk.Frame):
    def __init__(self, parent, controller, produto_id, callback_botao_voltar):
        super().__init__(parent, bg="#ffffff")

        self.controller = controller
        self.produto_id = produto_id
        self.callback_botao_voltar = callback_botao_voltar

        produto = self.controller.buscar_produto(produto_id)

        tk.Label(self, text="Editar Produto", font=("Arial", 20), bg="#ffffff").grid(row=0, column=0, columnspan=2)

        tk.Label(self, text="Nome:", bg="#ffffff").grid(row=1, column=0)
        self.inserir_nome = tk.Entry(self, width=20)
        self.inserir_nome.insert(0, produto[1])
        self.inserir_nome.grid(row=1, column=1)

        tk.Label(self, text="Categoria:", bg="#ffffff").grid(row=2, column=0)
        self.inserir_categoria = tk.Entry(self, width=20)
        self.inserir_categoria.insert(0, produto[2])
        self.inserir_categoria.grid(row=2, column=1)

        tk.Label(self, text="Quantidade:", bg="#ffffff").grid(row=3, column=0)
        self.inserir_quantidade = tk.Entry(self, width=20)
        self.inserir_quantidade.insert(0, produto[3])
        self.inserir_quantidade.grid(row=3, column=1)

        tk.Label(self, text="Preço:", bg="#ffffff").grid(row=4, column=0)
        self.inserir_preco = tk.Entry(self, width=20)
        self.inserir_preco.insert(0, produto[4])
        self.inserir_preco.grid(row=4, column=1)

        frame_botoes = tk.Frame(self, bg="#ffffff")
        frame_botoes.grid(row=5, column=0, columnspan=2, pady=10)

        tk.Button(frame_botoes, text="Salvar", command=self.salvar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botoes, text="Voltar", command=self.callback_botao_voltar).grid(row=0, column=1, padx=5)

    def pegar_dados(self):
        return {
            "nome": self.inserir_nome.get(),
            "categoria": self.inserir_categoria.get(),
            "quantidade": self.inserir_quantidade.get(),
            "preco": self.inserir_preco.get()
        }

    def salvar(self):
        dados = self.pegar_dados()
        self.controller.atualizar_produto(self.produto_id, dados)
        self.callback_botao_voltar()
