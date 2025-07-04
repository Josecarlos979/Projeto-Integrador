from db.connection import conector

class Cliente:
    def __init__(self, id_cliente=None, nome=None, email=None, telefone=None):
        self.id = id_cliente
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # CREATE / UPDATE
    def salvar(self):
        conn = conector(); cur = conn.cursor()
        if self.id is None:
            sql = "INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)"
            cur.execute(sql, (self.nome, self.email, self.telefone))
            self.id = cur.lastrowid
        else:
            sql = "UPDATE cliente SET nome=%s, email=%s, telefone=%s WHERE id_cliente=%s"
            cur.execute(sql, (self.nome, self.email, self.telefone, self.id))
        conn.commit(); conn.close()

    @staticmethod
    def buscar_todos():
        conn = conector(); cur = conn.cursor()
        cur.execute("SELECT id_cliente, nome, email, telefone FROM cliente")
        rows = cur.fetchall(); conn.close()
        return [Cliente(*row) for row in rows]
