from model import Model
from view import View
from controller import Controller
import model.database as Database

if __name__ == "__main__":
    Database.criar_tabela()
    print("Banco e tabela criados com sucesso!")