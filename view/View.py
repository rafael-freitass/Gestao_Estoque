from controller.Controller import Controller
import tkinter as tk
import tkinter.messagebox as messagebox

class View:
    def __init__(self):
        self.controller = Controller()
        self.root = tk.Tk()
        self.root.title("Gestão de Estoque")
        self.root.geometry("1000x600")

        # Container para barra lateral
        self.sideContiner = tk.Frame(self.root, width=900, height=600)
        self.sideContiner.pack(side="left", fill="y", padx=10, pady=10)

        # Container para tela principal
        self.mainContainer = tk.Frame(self.root, bg="#ffffff")
        self.mainContainer.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.sidebar(self.sideContiner)
        self.tela_estoque(self.mainContainer)

        self.root.mainloop()

    def tabela_estoque(self, container, controller):
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

        self.label_entrada_saida = tk.Label(container, text="ENTRADA/SAÍDA", bg="#ffffff", borderwidth=1, relief="solid", width=15)
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

            self.label_product_id = tk.Label(container, text=produto_id, bg="#ffffff", borderwidth=1, relief="solid", width=15)
            self.label_product_id.grid(row=actual_row, column=0, padx=1, pady=1)

            self.label_product_nome = tk.Label(container, text=nome, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_nome.grid(row=actual_row, column=1, padx=1, pady=1)

            self.label_product_categoria = tk.Label(container, text=categoria, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_categoria.grid(row=actual_row, column=2, padx=1, pady=1)

            self.label_product_qtd = tk.Label(container, text=quantidade, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_qtd.grid(row=actual_row, column=3, padx=1, pady=1)

            self.label_product_preco = tk.Label(container, text=preco, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_preco.grid(row=actual_row, column=4, padx=1, pady=1)

            self.frame_botoes = tk.Frame(container, bg="#ffffff")
            self.frame_botoes.grid(row=actual_row, column=5, columnspan=2)

            self.botao_entrada = tk.Button(self.frame_botoes, text="+", command= lambda pid=produto_id: controller.registrar_entrada(pid), width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_entrada.grid(row=actual_row, column=5, padx=1, pady=1)

            self.botao_saida = tk.Button(self.frame_botoes, text="-", command= lambda pid=produto_id: controller.registrar_saida(pid), width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_saida.grid(row=actual_row, column=6, padx=1, pady=1)
            actual_row += 1

    def tela_estoque(self, container):
        self.limpar_tela(container)

        container.rowconfigure(2, weight=1)
        self.titulo = tk.Label(container, text="ESTOQUE", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column= 0)

        self.frame_tabela = tk.Frame(container, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)

        self.info_vendas = self.titulo = tk.Label(container, text="Vendas do dia:", font=("Arial", 20), bg="#ffffff")
        self.info_vendas.grid(row=3, column=0)
        
        self.tabela_estoque(self.frame_tabela, self.controller)  

    def tabela_editar(self, container):
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

        self.label_entrada_saida = tk.Label(container, text="OPÇÕES", bg="#ffffff", borderwidth=1, relief="solid", width=15)
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

            self.label_product_id = tk.Label(container, text=produto_id, bg="#ffffff", borderwidth=1, relief="solid", width=15)
            self.label_product_id.grid(row=actual_row, column=0, padx=1, pady=1)

            self.label_product_nome = tk.Label(container, text=nome, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_nome.grid(row=actual_row, column=1, padx=1, pady=1)

            self.label_product_categoria = tk.Label(container, text=categoria, bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_categoria.grid(row=actual_row, column=2, padx=1, pady=1)

            self.label_product_qtd = tk.Label(container, text=quantidade, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_qtd.grid(row=actual_row, column=3, padx=1, pady=1)

            self.label_product_preco = tk.Label(container, text=preco, bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_preco.grid(row=actual_row, column=4, padx=1, pady=1)

            self.frame_botoes = tk.Frame(container, bg="#ffffff")
            self.frame_botoes.grid(row=actual_row, column=5, columnspan=2)

            self.botao_editar = tk.Button(self.frame_botoes, text="Editar", command= lambda pid=produto_id: self.chamar_tela_opcoes(pid), bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_editar.grid(row=actual_row, column=5, padx=1, pady=1)

            self.botao_excluir = tk.Button(self.frame_botoes, text="Excluir", command= lambda pid=produto_id: self.controller.excluir_produto(pid), width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_excluir.grid(row=actual_row, column=6, padx=1, pady=1)
            actual_row += 1

    def tela_editar(self, container):
        self.limpar_tela(container)

        container.rowconfigure(2, weight=1)
        self.titulo = tk.Label(container, text="EDITAR PRODUTOS", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column= 0)

        self.frame_tabela = tk.Frame(container, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)
        
        self.tabela_editar(self.frame_tabela)  

    def tela_opcoes(self, container, produto_id):
        self.limpar_tela(container)
        container.rowconfigure(2, weight=0)
        produto = self.controller.buscar_produto(produto_id)
        
        self.titulo = tk.Label(container, text="Editar Produto", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        self.nome = tk.Label(container, text="Nome: ", bg="#ffffff")
        self.nome.grid(row=1, column=0)

        self.inserir_nome = tk.Entry(container, width=20)
        self.inserir_nome.insert(0, produto[1])
        self.inserir_nome.grid(row=1,column=1)

        self.categoria = tk.Label(container, text="Categoria: ", bg="#ffffff")
        self.categoria.grid(row=2, column=0)

        self.inserir_categoria = tk.Entry(container, width=20)
        self.inserir_categoria.insert(0, produto[2])
        self.inserir_categoria.grid(row=2, column=1)

        self.quantidade = tk.Label(container, text="Categoria: ", bg="#ffffff")
        self.quantidade.grid(row=3, column=0)

        self.inserir_quantidade = tk.Entry(container, width=20)
        self.inserir_quantidade.insert(0, produto[3])
        self.inserir_quantidade.grid(row=3, column=1)

        self.preco = tk.Label(container, text="Preço: ", bg="#ffffff")
        self.preco.grid(row=4, column=0)

        self.inserir_preco = tk.Entry(container, width=20)
        self.inserir_preco.insert(0, produto[4])
        self.inserir_preco.grid(row=4, column=1)

        self.frame_botoes = tk.Frame(container, bg="#ffffff")
        self.frame_botoes.grid(row=5, column=1, columnspan=2)

        self.botao_voltar = tk.Button(self.frame_botoes, text='Voltar', command= self.chamar_tela_editar)
        self.botao_voltar.grid(row=0, column=1)

        self.botao_salvar_edit = tk.Button(self.frame_botoes, text='Salvar', command=lambda: self.controller.atualizar_produto(produto_id, self.pegar_dados()))
        self.botao_salvar_edit.grid(row=0, column=0)

    def tela_registrar(self, container, controller):
        self.limpar_tela(container)
        container.rowconfigure(2, weight=0)
        
        self.titulo = tk.Label(container, text="Registar Produto", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        self.nome = tk.Label(container, text="Nome:", bg="#ffffff")
        self.nome.grid(row=1, column=0)
        self.inserir_nome = tk.Entry(container, width=20, validate="key")
        self.inserir_nome.grid(row=1, column=1)

        self.categoria = tk.Label(container, text="Categoria:", bg="#ffffff")
        self.categoria.grid(row=2, column=0)
        self.inserir_categoria = tk.Entry(container, width=20, validate="key")
        self.inserir_categoria.grid(row=2, column=1)

        self.quantidade = tk.Label(container, text="Quantidade:", bg="#ffffff")
        self.quantidade.grid(row=3, column=0)
        self.inserir_quantidade = tk.Entry(container, width=20, validate="key")
        self.inserir_quantidade.grid(row=3, column=1)

        self.preco = tk.Label(container, text="Preco:", bg="#ffffff")
        self.preco.grid(row=4, column=0)
        self.inserir_preco = tk.Entry(container, width=20, validate="key")
        self.inserir_preco.grid(row=4, column=1)

        self.frame_botoes = tk.Frame(container, bg="#ffffff")
        self.frame_botoes.grid(row=5, column=1, columnspan=2)
        
        self.botao_limpar = tk.Button(self.frame_botoes, text='Limpar', command= self.limpar_textos)
        self.botao_limpar.grid(row=0, column=0)

        self.botao_salvar = tk.Button(self.frame_botoes, text='Salvar', command= lambda: controller.registrar_produto(self.pegar_dados()))
        self.botao_salvar.grid(row=0, column=1)

    def limpar_textos(self):
        pass

    def pegar_dados(self):
        return {
        "nome" : self.inserir_nome.get(),
        "categoria" : self.inserir_categoria.get(),
        "quantidade" : self.inserir_quantidade.get(),
        "preco" : self.inserir_preco.get()
        }

    def limpar_tela(self, container):
        for widget in container.winfo_children():
            widget.destroy()

    def chamar_tela_estoque(self):
        self.tela_estoque(self.mainContainer)

    def chamar_tela_editar(self):
        self.tela_editar(self.mainContainer)

    def chamar_tela_opcoes(self, produto_id):
        self.tela_opcoes(self.mainContainer, produto_id)

    def chamar_tela_registro(self):
        self.tela_registrar(self.mainContainer, self.controller)

    def sidebar(self, container):
        container.rowconfigure(3, weight=1)

        self.botao_estoque = tk.Button(container, text="Estoque", bg="#34495e", fg="white",
                  command=self.chamar_tela_estoque)
        self.botao_estoque.grid(row= 0, column= 0, sticky="ew")

        self.botao_editar = tk.Button(container, text="Editar Produto", bg="#34495e", fg="white",
                  command=self.chamar_tela_editar)
        self.botao_editar.grid(row=1, column=0, sticky="ew")

        self.botao_registrar = tk.Button(container, text="Registrar Produto", bg="#34495e", fg="white",
                  command=self.chamar_tela_registro)
        self.botao_registrar.grid(row=2, column=0, sticky="ew")

        self.botao_sair = tk.Button(container, text="Sair", bg="#e74c3c", fg="white",
                  command=self.root.quit)
        self.botao_sair.grid(row=4, column=0, sticky="ew")