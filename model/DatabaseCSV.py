import csv
from datetime import datetime

class Database_CSV:
    def __init__(self):
        data_atual = datetime.now().strftime("%d-%m-%Y")
        self.path = f"controle_caixa_{data_atual}.csv"
        self.criar_planilha()

    def criar_planilha(self):
        try:
            with open(self.path, 'x', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["data_hora", "nome_produto", "quantidade", "valor_unitario", "tipo"])
        except FileExistsError:
            pass

    def registrar_entrada(self, nome_produto, quantidade, valor_unitario):
        self.escrever_tabela("entrada", nome_produto, quantidade, valor_unitario)

    def registrar_saida(self, nome_produto, quantidade, valor_unitario):
        self.escrever_tabela("saida", nome_produto, quantidade, valor_unitario)

    def escrever_tabela(self, tipo, nome_produto, quantidade, valor_unitario):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open(self.path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([data_hora, nome_produto, quantidade, valor_unitario, tipo])

    def calcular_total_saidas(self):
        total = 0.0
        with open(self.path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['tipo'] == 'saida':
                    quantidade = float(row['quantidade'])
                    valor_unitario = float(row['valor_unitario'])
                    total += quantidade * valor_unitario
            return total