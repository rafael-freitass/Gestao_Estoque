import tkinter as tk
import tkinter.messagebox as messagebox

class Tela_estoque(tk.Frame):
    def __init__(self, parent, controller_view):
        super().__init__(parent, bg="#ffffff")
        self.controller_view = controller_view
        self.controller = controller_view.controller

        self.rowconfigure(2, weight=1)

        # título do frame
        self.titulo = tk.Label(self, text="ESTOQUE", font=("Arial", 20), bg="#ffffff")
        self.titulo.grid(row=0, column=0)

        # frame da tabela de produtos
        self.frame_tabela = tk.Frame(self, bg="#ffffff")
        self.frame_tabela.grid(row=1, column=0)

        # vendas do dia
        self.info_vendas = tk.Label(self, text="Vendas do dia:", font=("Arial", 20), bg="#ffffff")
        self.info_vendas.grid(row=3, column=0)
        
        self.tabela_estoque()

    def tabela_estoque(self):
        container = self.frame_tabela

        headers = ["ID", "NOME", "CATEGORIA", "QTD", "PREÇO", "ENTRADA/SAÍDA"]
        for idx, text in enumerate(headers):
            label = tk.Label(container, text=text, bg="#ffffff", borderwidth=1, relief="solid", width=15)
            label.grid(row=0, column=idx, padx=1, pady=1)

        # Carrega os produtos
        lista_produtos = self.controller.produtos_em_estoque()
        actual_row = 1

        for product in lista_produtos:
            produto_id, nome, categoria, quantidade, preco = product

            # Dados do produto
            dados = [produto_id, nome, categoria, quantidade, preco]
            for col, value in enumerate(dados):
                tk.Label(container, text=value, bg="#ffffff", borderwidth=1, relief="solid", width=15).grid(row=actual_row, column=col, padx=1, pady=1)

            # Botões Entrada/Saída
            frame_botoes = tk.Frame(container, bg="#ffffff")
            frame_botoes.grid(row=actual_row, column=5, columnspan=2)

            tk.Button(frame_botoes, text="+", command=lambda pid=produto_id: self.controller.registrar_entrada(pid),
                      width=2, bg="#ffffff", borderwidth=1, relief="solid").pack(side="left", padx=1)

            tk.Button(frame_botoes, text="-", command=lambda pid=produto_id: self.controller.registrar_saida(pid),
                      width=2, bg="#ffffff", borderwidth=1, relief="solid").pack(side="left", padx=1)

            actual_row += 1
