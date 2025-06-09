import sqlite3

def criar_conexao():
    conectar = sqlite3.connect("banco_estoque.db")  # cria o arquivo meubanco.db automaticamente
    return conectar

def criar_tabela():
    conectar = criar_conexao()
    cursor = conectar.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            categoria VARCHAR(255) NOT NULL,
            quantidade INTEGER NOT NULL,
            preco DOUBLE NOT NULL   
        )
    """)
    conectar.commit()
    conectar.close()

def inserir_dados():
    conectar = criar_conexao()
    cursor = conectar.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(255) NOT NULL,
            categoria VARCHAR(255) NOT NULL,
            quantidade INTEGER NOT NULL,
            preco DOUBLE NOT NULL   
        )
    """)
    conectar.commit()
    conectar.close()