from controller import Controller
import tkinter as tk

class View:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestão de Estoque")
        self.root.geometry("900x600")

        # Container para barra lateral
        self.sideContiner = tk.Frame(self.root, width=900, height=600)
        self.sideContiner.pack(side="left", fill="y", padx=10, pady=10)

        # Container para tela principal
        self.mainContainer = tk.Frame(self.root, bg="#ffffff")
        self.mainContainer.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.sidebar(self.sideContiner)
        self.tela_estoque(self.mainContainer)

        self.root.mainloop()

    def tela_estoque(self, container):
        self.limpar_tela(container)

        container.rowconfigure(2, weight=1)
        self.titulo = tk.Label(container, text="ESTOQUE", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column= 0)

        self.frame_tabela = tk.Frame(container, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)

        self.info_vendas = self.titulo = tk.Label(container, text="Vendas do dia:", font=("Arial", 20), bg="#ffffff")
        self.info_vendas.grid(row=3, column=0)
        
        self.tabela_opcoes(self.frame_tabela)  

    def tabela_opcoes(self, container):
        self.label_id = tk.Label(container, text="ID", bg="#ffffff", borderwidth=1, relief="solid", width=15)
        self.label_id.grid(row=0, column=0, padx=1, pady=1)

        self.label_nome = tk.Label(container, text="NOME", bg="#ffffff", borderwidth=1, relief="solid", width=20)
        self.label_nome.grid(row=0, column=1, padx=1, pady=1)

        self.label_categoria = tk.Label(container, text="CATEGORIA", bg="#ffffff", borderwidth=1, relief="solid", width=20)
        self.label_categoria.grid(row=0, column=2, padx=1, pady=1)

        self.label_quantidade = tk.Label(container, text="QTD", bg="#ffffff", borderwidth=1, relief="solid", width=10)
        self.label_quantidade.grid(row=0, column=3, padx=1, pady=1)

        self.label_entrada_saida = tk.Label(container, text="ENTRADA/SAÍDA", bg="#ffffff", borderwidth=1, relief="solid", width=15)
        self.label_entrada_saida.grid(row=0, column=4, padx=1, pady=1)

        #Carrega dados

        lista_produtos = [
            {
                "id": 1,
                "nome": "Mouse Gamer",
                "categoria": "Periféricos",
                "quantidade": 25
            },
            {
                "id": 2,
                "nome": "Teclado Mecânico",
                "categoria": "Periféricos",
                "quantidade": 15
            },
            {
                "id": 3,
                "nome": "Monitor 24 Polegadas",
                "categoria": "Monitores",
                "quantidade": 8
            }
        ]
        actual_row = 1
        for product in lista_produtos:
            self.label_product_id = tk.Label(container, text=product.get('id'), bg="#ffffff", borderwidth=1, relief="solid", width=15)
            self.label_product_id.grid(row=actual_row, column=0, padx=1, pady=1)

            self.label_product_nome = tk.Label(container, text=product.get('nome'), bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_nome.grid(row=actual_row, column=1, padx=1, pady=1)

            self.label_product_categoria = tk.Label(container, text=product.get('categoria'), bg="#ffffff", borderwidth=1, relief="solid", width=20)
            self.label_product_categoria.grid(row=actual_row, column=2, padx=1, pady=1)

            self.label_product_qtd = tk.Label(container, text=product.get('quantidade'), bg="#ffffff", borderwidth=1, relief="solid", width=10)
            self.label_product_qtd.grid(row=actual_row, column=3, padx=1, pady=1)

            self.frame_botoes = tk.Frame(container, bg="#ffffff")
            self.frame_botoes.grid(row=actual_row, column=4, columnspan=2)

            self.botao_entrada = tk.Button(self.frame_botoes, text="+", width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_entrada.grid(row=actual_row, column=4, padx=1, pady=1)

            self.botao_saida = tk.Button(self.frame_botoes, text="-", width=2, bg="#ffffff", borderwidth=1, relief="solid")
            self.botao_saida.grid(row=actual_row, column=5, padx=1, pady=1)
            actual_row += 1

    def tela_editar(self, container):
        self.limpar_tela(container)
        tk.Label(container, text="Tela Editar Estoque", font=("Arial", 20), bg="#ffffff").pack(pady=20)

    def tela_registrar(self, container):
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

        self.botao_limpar = tk.Button(self.frame_botoes, text='Limpar')
        self.botao_limpar.grid(row=0, column=0)

        self.botao_salvar = tk.Button(self.frame_botoes, text='Salvar')
        self.botao_salvar.grid(row=0, column=1)

    def limpar_tela(self, container):
        for widget in container.winfo_children():
            widget.destroy()

    def chamar_tela_estoque(self):
        self.tela_estoque(self.mainContainer)

    def chamar_tela_editar(self):
        self.tela_editar(self.mainContainer)

    def chamar_tela_registro(self):
        self.tela_registrar(self.mainContainer)

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

if __name__ == "__main__":
    View()