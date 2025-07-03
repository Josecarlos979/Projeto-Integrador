import mysql.connector

def conector():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='984641940',
        database='restaurante_db'
    )