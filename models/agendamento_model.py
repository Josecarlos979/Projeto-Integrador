from db.connection import conector

class Agendamento:
    def __init__(self, id_agendamento=None, id_evento=None, id_cliente=None, id_funcionario=None, data_hora=None):
        self.id = id_agendamento
        self.id_evento = id_evento
        self.id_cliente = id_cliente
        self.id_funcionario = id_funcionario
        self.data_hora = data_hora  # string 'YYYY-MM-DD HH:MM:SS'

    def salvar(self):
        conn = conector(); cur = conn.cursor()
        if self.id is None:
            cur.execute(
                """INSERT INTO agendamento (id_evento, id_cliente, id_funcionario, data_hora)
                   VALUES (%s, %s, %s, %s)""",
                (self.id_evento, self.id_cliente, self.id_funcionario, self.data_hora)
            )
            self.id = cur.lastrowid
        else:
            cur.execute(
                """UPDATE agendamento
                   SET id_evento=%s, id_cliente=%s, id_funcionario=%s, data_hora=%s
                   WHERE id_agendamento=%s""",
                (self.id_evento, self.id_cliente, self.id_funcionario, self.data_hora, self.id)
            )
        conn.commit(); conn.close()

    @staticmethod
    def buscar_todos():
        conn = conector(); cur = conn.cursor()
        cur.execute(
            """SELECT id_agendamento, id_evento, id_cliente, id_funcionario, data_hora
               FROM agendamento"""
        )
        rows = cur.fetchall(); conn.close()
        return [Agendamento(*row) for row in rows]
