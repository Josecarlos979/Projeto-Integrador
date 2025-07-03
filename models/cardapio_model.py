from db.connection import conector


class Cardapio:
    """
    Representa um único item de cardápio.
    """

    def __init__(self, id_cardapio=None, nome_item=None, descricao_item=None):
        self.id = id_cardapio
        self.nome_item = nome_item
        self.descricao_item = descricao_item

    # ---------- Métodos de Instância ---------- #
    def salvar(self):
        """
        Insere OU atualiza dependendo se self.id está definido.
        """
        with conector() as conn:
            cursor = conn.cursor()

            if self.id is None:
                sql = """INSERT INTO cardapio (nome_item, descricao_item)
                         VALUES (%s, %s)"""
                cursor.execute(sql, (self.nome_item, self.descricao_item))
                self.id = cursor.lastrowid
            else:
                sql = """UPDATE cardapio
                         SET nome_item = %s, descricao_item = %s
                         WHERE id_cardapio = %s"""
                cursor.execute(sql, (self.nome_item,
                                     self.descricao_item,
                                     self.id))

    # ---------- Métodos de Classe ---------- #
    @classmethod
    def buscar_todos(cls):
        with conector() as conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT id_cardapio, nome_item, descricao_item "
                           "FROM cardapio ORDER BY id_cardapio DESC")
            rows = cursor.fetchall()
            return [cls(**row) for row in rows]