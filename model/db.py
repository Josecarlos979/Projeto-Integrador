import mysql.connector
from mysql.connector import Error

def conectaDB():
    try:
        conexao = mysql.connector.connect(
            host='localhost',       
            user='root',     
            password='984641940',  
            database='restaurante'  
        )

        if conexao.is_connected():
            print("Logou")
            return conexao

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    
conectaDB()