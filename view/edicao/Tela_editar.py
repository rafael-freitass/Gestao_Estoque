from controller.Controller import Controller
import tkinter as tk
import tkinter.messagebox as messagebox

class Tela_editar(tk.Frame):
    def __init__(self, parent, controller_view):
        super().__init__(parent, bg="#ffffff")
        self.controller_view = controller_view
        self.controller = controller_view.controller

        self.rowconfigure(2, weight=1)

        # Titulo
        self.titulo = tk.Label(self, text="EDITAR PRODUTOS", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column= 0)

        # Frame da Tabela
        self.frame_tabela = tk.Frame(self, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)
        
        self.tabela_editar(self.frame_tabela)  
    

    def tabela_editar(self, frame_tabela):
        self.label_id = tk.Label(self, text="ID", bg="#ffffff", borderwidth=1, relief="solid", width=15)
        self.label_id.grid(row=0, column=0, padx=1, pady=1)

        self.label_nome = tk.Label(self, text="NOME", bg="#ffffff", borderwidth=1, relief="solid", width=20)
        self.label_nome.grid(row=0, column=1, padx=1, pady=1)

        self.label_categoria = tk.Label(self, text="CATEGORIA", bg="#ffffff", borderwidth=1, relief="solid", width=20)
        self.label_categoria.grid(row=0, column=2, padx=1, pady=1)

        self.label_quantidade = tk.Label(self, text="QTD", bg="#ffffff", borderwidth=1, relief="solid", width=10)
        self.label_quantidade.grid(row=0, column=3, padx=1, pady=1)

        self.label_preco = tk.Label(self, text="PREÇO", bg="#ffffff", borderwidth=1, relief="solid", width=10)
        self.label_preco.grid(row=0, column=4, padx=1, pady=1)

        self.label_entrada_saida = tk.Label(self, text="OPÇÕES", bg="#ffffff", borderwidth=1, relief="solid", width=15)
        self.label_entrada_saida.grid(row=0, column=5, padx=1, pady=1)

        #Carrega dados

        lista_produtos = self.controller.produtos_em_estoque()
        actual_row = 1
        for product in lista_produtos:
            produto_id = product[0]
            nome = product[1]
            categoria = product[2]
            quantidade = product[3]
            preco = product[4]

            self.label_product_id = tk.Label(self, text=produto_id, bg="#ffffff", borderwidth=1, relief="solid", width=15)
            self.label_product_id.grid(row=actual_row, column=0, padx=1, pady=1)

            self.label_product_nome = tk.Label(self, text=nome, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_nome.grid(row=actual_row, column=1, padx=1, pady=1)

            self.label_product_categoria = tk.Label(self, text=categoria, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_categoria.grid(row=actual_row, column=2, padx=1, pady=1)

            self.label_product_qtd = tk.Label(self, text=quantidade, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_qtd.grid(row=actual_row, column=3, padx=1, pady=1)

            self.label_product_preco = tk.Label(self, text=preco, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_preco.grid(row=actual_row, column=4, padx=1, pady=1)

            self.frame_botoes = tk.Frame(self, bg="#ffffff")
            self.frame_botoes.grid(row=actual_row, column=5, columnspan=2)

            self.botao_editar = tk.Button(self.frame_botoes, text="Editar", command= lambda pid=produto_id: self.chamar_tela_opcoes(pid), bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_editar.grid(row=actual_row, column=5, padx=1, pady=1)

            self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command= lambda pid=produto_id: self.controller.excluir_produto(pid), width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_excluir.grid(row=actual_row, column=6, padx=1, pady=1)
            actual_row += 1


    def tela_opcoes(self, produto_id):
        self.rowconfigure(2, weight=0)
        produto = self.controller.buscar_produto(produto_id)
        
        self.titulo = tk.Label(self, text="Editar Produto", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        self.nome = tk.Label(self, text="Nome: ", bg="#ffffff")
        self.nome.grid(row=1, column=0)

        self.inserir_nome = tk.Entry(self, width=20)
        self.inserir_nome.insert(0, produto[1])
        self.inserir_nome.grid(row=1,column=1)

        self.categoria = tk.Label(self, text="Categoria: ", bg="#ffffff")
        self.categoria.grid(row=2, column=0)

        self.inserir_categoria = tk.Entry(self, width=20)
        self.inserir_categoria.insert(0, produto[2])
        self.inserir_categoria.grid(row=2, column=1)

        self.quantidade = tk.Label(self, text="Categoria: ", bg="#ffffff")
        self.quantidade.grid(row=3, column=0)

        self.inserir_quantidade = tk.Entry(self, width=20)
        self.inserir_quantidade.insert(0, produto[3])
        self.inserir_quantidade.grid(row=3, column=1)

        self.preco = tk.Label(self, text="Preço: ", bg="#ffffff")
        self.preco.grid(row=4, column=0)

        self.inserir_preco = tk.Entry(self, width=20)
        self.inserir_preco.insert(0, produto[4])
        self.inserir_preco.grid(row=4, column=1)

        self.frame_botoes = tk.Frame(self, bg="#ffffff")
        self.frame_botoes.grid(row=5, column=1, columnspan=2)

        self.botao_voltar = tk.Button(self.frame_botoes, text='Voltar', command= self.chamar_tela_editar)
        self.botao_voltar.grid(row=0, column=1)

        self.botao_salvar_edit = tk.Button(self.frame_botoes, text='Salvar', command=lambda: self.controller.atualizar_produto(produto_id, self.pegar_dados()))
        self.botao_salvar_edit.grid(row=0, column=0)

