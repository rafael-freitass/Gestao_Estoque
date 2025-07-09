import sqlite3

class Database_SQLite:

    def __init__(self):
        self.criar_tabela()

    def criar_conexao(self):
        return sqlite3.connect("banco_estoque.db")

    def criar_tabela(self):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                categoria VARCHAR(255) NOT NULL,
                quantidade INTEGER NOT NULL,
                preco DOUBLE NOT NULL   
            )
        """)
        self.conn.commit()
        self.conn.close()

    def registrar_produto(self, valores):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Produto (nome, categoria, quantidade, preco)
                VALUES (?, ?, ?, ?)
            """, (
                valores['nome'],
                valores['categoria'],
                int(valores['quantidade']),
                float(valores['preco'])
            ))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def listar_produtos_estoque(self):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * from Produto
            WHERE Produto.quantidade > -1
            LIMIT 10
        """)
        produtos = cursor.fetchall()
        self.conn.close()
        return produtos

    def registrar_entrada(self, id):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                UPDATE Produto
                SET quantidade = quantidade + 1
                WHERE id = ?
            """, (id,))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def registrar_saida(self, id):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT quantidade FROM Produto WHERE id = ?", (id,))
            resultado = cursor.fetchone()
            if resultado and resultado[0] > 0:
                cursor.execute("""
                    UPDATE Produto
                    SET quantidade = quantidade - 1
                    WHERE id = ?
                """, (id,))
                self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def buscar_produto(self, id):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * from Produto
            WHERE id = ?
        """, (id,))
        produto = cursor.fetchone()
        self.conn.close()
        return produto

    def atualizar_produto(self, id, dados):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                UPDATE Produto
                SET nome = ?, categoria = ?, quantidade = ?, preco = ?
                WHERE id = ?
            """, (
                dados['nome'],
                dados['categoria'],
                int(dados['quantidade']),
                float(dados['preco']),
                id
            ))
            self.conn.commit()
            self.conn.close()
            return True
        except:
            return False

    def excluir_produto(self, id):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        cursor.execute("""
                    DELETE 
                    FROM Produto 
                    WHERE id = ?
                """, (id,))
        self.conn.commit()
        self.conn.close()

    def buscar_quantidade_produto(self, produto_id):
        self.conn = self.criar_conexao()
        cursor = self.conn.cursor()
        cursor.execute("""
                    SELECT quantidade 
                    FROM Produto
                    WHERE id = ?
                """,(produto_id,))
        qtd_produto = cursor.fetchone()
        self.conn.close()
        return qtd_produto[0]
