import sqlite3

def criar_conexao():
    return sqlite3.connect("banco_estoque.db")    

def criar_tabela():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            categoria VARCHAR(255) NOT NULL,
            quantidade INTEGER NOT NULL,
            preco DOUBLE NOT NULL   
        )
    """)
    conn.commit()
    conn.close()

def registrar_produto(valores):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Produto (nome, categoria, quantidade, preco)
        VALUES (?, ?, ?, ?)
    """, (
        valores['nome'],
        valores['categoria'],
        int(valores['quantidade']),
        float(valores['preco'])
    ))
    conn.commit()
    print("Produto Salvo no banco com sucesso!")
    conn.close()

def listar_produtos_estoque():
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * from Produto
        WHERE Produto.quantidade > 0
    """)
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def registrar_entrada(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Produto
        SET quantidade = quantidade + 1
        WHERE id = ?
    """, (id,))
    conn.commit()
    print("Entrada Registrada no banco com sucesso!")
    conn.close()

def registrar_saida(id):
    conn = criar_conexao()
    cursor = conn.cursor()

    cursor.execute("SELECT quantidade FROM Produto WHERE id = ?", (id,))
    resultado = cursor.fetchone()

    if resultado and resultado[0] > 0:
        cursor.execute("""
            UPDATE Produto
            SET quantidade = quantidade - 1
            WHERE id = ?
        """, (id,))
        conn.commit()
        sucesso = True
    else:
        sucesso = False
    print("Saida Registrada no banco com sucesso!")
    conn.close()
    return sucesso

def buscar_produto(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * from Produto
        WHERE id = ?
    """, (id,))
    produto = cursor.fetchone()
    conn.close()
    return produto

def atualizar_produto(id, dados):
    conn = criar_conexao()
    cursor = conn.cursor()
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
    conn.commit()
    print("Produto Atualizado no banco com sucesso!")
    conn.close()

def excluir_produto(id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
                DELETE 
                FROM Produto 
                WHERE id = ?
            """, (id,))
    conn.commit()
    print("Produto Excluido no banco com sucesso!")
    conn.close()

def buscar_quantidade_produto(produto_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    cursor.execute("""
                SELECT quantidade 
                FROM Produto
                WHERE id = ?
            """,(produto_id,))
    qtd_produto = cursor.fetchone()
    conn.close()
    return qtd_produto[0]
