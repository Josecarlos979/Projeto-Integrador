from models.db import conector

class Cardapio:
    def __init__(self, id_cardapio=None, nome_item=None, descricao_item=None):
        self.id = id_cardapio
        self.nome_item = nome_item
        self.descricao_item = descricao_item

    def salvar(self):
        conn = conector()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO cardapio (nome_item, descricao_item) VALUES (%s, %s)"
            valores = (self.nome_item, self.descricao_item)
        else:
            sql = "UPDATE cardapio SET nome_item = %s, descricao_item = %s WHERE id_cardapio = %s"
            valores = (self.nome_item, self.descricao_item, self.id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conector()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM cardapio")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()

        return resultados
