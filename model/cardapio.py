from model.cardapio import conector

class Cardapio: 
    def __innit__(self,id,numero, nome_do_pedido, descricao):
        self.id = id
        self.numero = numero 
        self.nome_do_pedido = nome_do_pedido 
        self.descricao = descricao 

    def salvar (self):
        conn = conector()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO cardapio (id, numero, nome_do_pedido, descricao) VALUES (%s,%s,%s)"
            valores = (self.id, self.numero, self.nome_do_pedido, self.descricao)

        else:
            sql = "UPDATE cardapio SET numero= %s, nome_do_pedido = %s, descricao = %s"
            valores = (self.id, self.numero, self.nome_do_pedido, self.descricao)

        cursor.execute (sql, valores)
        conn.commit()
        cursor.close()
        conn.close()


        @staticmethod
        def buscar_todos():
            conn = conector()
            cursor = conn.cursor ( dictinary = True )

            cursor.execute ("SELECT * FROM  Cardapio") 
            conn = cursor.fetchall()
 