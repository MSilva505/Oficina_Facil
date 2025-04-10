import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # Altere conforme a configuração do seu MySQL
            user='seu_usuario',  # Seu usuário do MySQL
            password='sua_senha',  # Sua senha do MySQL
            database='nome_do_banco'  # Nome do banco de dados
        )
        if connection.is_connected():
            print("Conexão com o banco de dados foi estabelecida!")
            return connection
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None
