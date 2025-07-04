from db.connection import conector

class Funcionario:
    def __init__(self, id_funcionario=None, nome=None, email=None, cargo=None):
        self.id = id_funcionario
        self.nome = nome
        self.email = email
        self.cargo = cargo

    def salvar(self):
        conn = conector(); cur = conn.cursor()
        if self.id is None:
            cur.execute(
                "INSERT INTO funcionario (nome, email, cargo) VALUES (%s, %s, %s)",
                (self.nome, self.email, self.cargo)
            )
            self.id = cur.lastrowid
        else:
            cur.execute(
                "UPDATE funcionario SET nome=%s, email=%s, cargo=%s WHERE id_funcionario=%s",
                (self.nome, self.email, self.cargo, self.id)
            )
        conn.commit(); conn.close()

    @staticmethod
    def buscar_todos():
        conn = conector(); cur = conn.cursor()
        cur.execute("SELECT id_funcionario, nome, email, cargo FROM funcionario")
        rows = cur.fetchall(); conn.close()
        return [Funcionario(*row) for row in rows]
