import tkinter as tk

class Tabela_produtos(tk.Frame):
    def __init__(self, parent, controller, tipo_tabela, callback_botao_editar=None):
        super().__init__(parent, bg="#ffffff")
        
        self.controller = controller
        self.tipo_tabela = tipo_tabela 
        self.callback_botao_editar = callback_botao_editar

        self.label_quantidade = {}

        self.montar_tabela()

    def montar_tabela(self):
        container = self

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
        
        if self.tipo_tabela == "estoque":
            self.label_entrada_saida = tk.Label(container, text="ENTRADA/SAIDA", bg="#ffffff", borderwidth=1, relief="solid", width=15)
            self.label_entrada_saida.grid(row=0, column=5, padx=1, pady=1)
        
        elif self.tipo_tabela == "editar":
            self.label_entrada_saida = tk.Label(container, text="OPÇÕES", bg="#ffffff", borderwidth=1, relief="solid", width=15)
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
            
            if self.tipo_tabela == "estoque":
                self.botao_adicionar = tk.Button(self.frame_botoes, text="+", command= lambda pid=produto_id: self.adicionar_e_atualizar(pid), width=6, bg="#ffffff", borderwidth=1, relief="solid")
                self.botao_adicionar.grid(row=actual_row, column=5, padx=1, pady=1)

                self.botao_diminuir = tk.Button(self.frame_botoes, text="-", command= lambda pid=produto_id: self.diminuir_e_atualizar(pid), width=6, bg="#ffffff", borderwidth=1, relief="solid")
                self.botao_diminuir.grid(row=actual_row, column=6, padx=1, pady=1)
            
            elif self.tipo_tabela == "editar":
                self.botao_editar = tk.Button(self.frame_botoes, text="Editar", command=lambda pid=produto_id: self.callback_botao_editar(pid), width=6, bg="#ffffff", borderwidth=1, relief="solid")
                self.botao_editar.grid(row=actual_row, column=5, padx=1, pady=1)

                self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command= lambda pid=produto_id: self.excluir_e_atualizar(pid), width=6, bg="#ffffff", borderwidth=1, relief="solid")
                self.botao_excluir.grid(row=actual_row, column=6, padx=1, pady=1)
            
            actual_row += 1
    
    def atualizar_tabela(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.montar_tabela()

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

    def excluir_e_atualizar(self, produto_id):
        self.controller.excluir_produto(produto_id)
        self.atualizar_tabela()
        