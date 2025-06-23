import tkinter as tk

class Tela_estoque(tk.Frame):
    def __init__(self, parent, controller_view):
        super().__init__(parent, bg="#ffffff")
        self.controller_view = controller_view
        self.controller = controller_view.controller

        self.rowconfigure(2, weight=1)

        # título da tela
        self.titulo = tk.Label(self, text="ESTOQUE", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        # frame da tabela de produtos
        self.frame_tabela = tk.Frame(self, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)

        # texto para qtd de vendas no dia
        self.info_vendas = tk.Label(self, text="Vendas do dia:", font=("Arial", 20), bg="#ffffff")
        self.info_vendas.grid(row=3, column=0)

        self.tabela_estoque()

    def tabela_estoque(self):
        container = self.frame_tabela

        # headers da tabela
        self.label_id = tk.Label(container, text="ID", bg="#ffffff", borderwidth=1, relief="solid", width=15)
        self.label_id.grid(row=0, column=0, padx=1, pady=1)

        self.label_nome = tk.Label(container, text="NOME", bg="#ffffff", borderwidth=1, relief="solid", width=20)
        self.label_nome.grid(row=0, column=1, padx=1, pady=1)

        self.label_categoria = tk.Label(container, text="CATEGORIA", bg="#ffffff", borderwidth=1, relief="solid", width=20)
        self.label_categoria.grid(row=0, column=2, padx=1, pady=1)

        self.label_quantidade = tk.Label(container, text="QTD", bg="#ffffff", borderwidth=1, relief="solid", width=10)
        self.label_quantidade.grid(row=0, column=3, padx=1, pady=1)

        self.label_preco = tk.Label(container, text="PREÇO", bg="#ffffff", borderwidth=1, relief="solid", width=10)
        self.label_preco.grid(row=0, column=4, padx=1, pady=1)

        self.label_entrada_saida = tk.Label(container, text="ENTRADA/SAIDA", bg="#ffffff", borderwidth=1, relief="solid", width=15)
        self.label_entrada_saida.grid(row=0, column=5, padx=1, pady=1)
        
        # carrega lista de produtos
        lista_produtos = self.controller.produtos_em_estoque()

        self.label_quantidade = {}

        actual_row = 1
        for product in lista_produtos:
            produto_id = product[0]
            nome = product[1]
            categoria = product[2]
            quantidade = product[3]
            preco = product[4]

            # monta tabela com lista de produtos
            self.label_product_id = tk.Label(container, text=produto_id, bg="#ffffff", borderwidth=1, relief="solid", width=15)
            self.label_product_id.grid(row=actual_row, column=0, padx=1, pady=1)

            self.label_product_nome = tk.Label(container, text=nome, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_nome.grid(row=actual_row, column=1, padx=1, pady=1)

            self.label_product_categoria = tk.Label(container, text=categoria, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_categoria.grid(row=actual_row, column=2, padx=1, pady=1)

            self.label_product_qtd = tk.Label(container, text=quantidade, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_qtd.grid(row=actual_row, column=3, padx=1, pady=1)
            self.label_quantidade[produto_id] = self.label_product_qtd

            self.label_product_preco = tk.Label(container, text=preco, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_preco.grid(row=actual_row, column=4, padx=1, pady=1)

            self.frame_botoes = tk.Frame(container, bg="#ffffff")
            self.frame_botoes.grid(row=actual_row, column=5, columnspan=2)

            self.botao_adicionar = tk.Button(self.frame_botoes, text="+", command= lambda pid=produto_id: self.adicionar_e_atualizar(pid), width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_adicionar.grid(row=actual_row, column=5, padx=1, pady=1)

            self.botao_diminuir = tk.Button(self.frame_botoes, text="-", command= lambda pid=produto_id: self.diminuir_e_atualizar(pid), width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_diminuir.grid(row=actual_row, column=6, padx=1, pady=1)
            actual_row += 1
    
    def atualizar_quantidade(self, produto_id):
        nova_quantidade = self.controller.buscar_quantidade(produto_id)
        label = self.label_quantidade.get(produto_id)
        label.config(text=str(nova_quantidade))

    def adicionar_e_atualizar(self, produto_id):
        self.controller.registrar_entrada(produto_id)
        self.atualizar_quantidade(produto_id)

    def diminuir_e_atualizar(self, produto_id):
        self.controller.registrar_saida(produto_id)
        self.atualizar_quantidade(produto_id)