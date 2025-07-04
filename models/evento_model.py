from db.connection import conector

class Evento:
    def __init__(self, id_evento=None, titulo=None, descricao=None, data=None):
        self.id = id_evento
        self.titulo = titulo
        self.descricao = descricao
        self.data = data  # string 'YYYY-MM-DD' ou datetime.date

    def salvar(self):
        conn = conector(); cur = conn.cursor()
        if self.id is None:
            cur.execute(
                "INSERT INTO evento (titulo, descricao, data_evento) VALUES (%s, %s, %s)",
                (self.titulo, self.descricao, self.data)
            )
            self.id = cur.lastrowid
        else:
            cur.execute(
                "UPDATE evento SET titulo=%s, descricao=%s, data_evento=%s WHERE id_evento=%s",
                (self.titulo, self.descricao, self.data, self.id)
            )
        conn.commit(); conn.close()

    @staticmethod
    def buscar_todos():
        conn = conector(); cur = conn.cursor()
        cur.execute("SELECT id_evento, titulo, descricao, data_evento FROM evento")
        rows = cur.fetchall(); conn.close()
        return [Evento(*row) for row in rows]
