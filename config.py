# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost/oficina_facil'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
<<<<<<< HEAD
    
    class Config:
    DB_HOST = 'localhost'
    DB_USER = 'seu_usuario'
    DB_PASSWORD = 'sua_senha'
    DB_NAME = 'nome_do_banco'

import mysql.connector
from config import Config

def create_connection():
    return mysql.connector.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )

def listar_oficinas():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM oficinas")
    oficinas = cursor.fetchall()
    connection.close()
    return oficinas

# Outras funções de banco (adicionar, atualizar, deletar) seguem a mesma estrutura.

=======
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    
    @staticmethod
    def init_app(app):
        # Criar pasta de uploads se não existir
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)
>>>>>>> 1c2b2be5b51ca8e88778e53eff19169b4d4f7f47
