# controllers/agendamento_controller.py
from models.agendamento_model import Agendamento

def agendar_evento(id_evento, id_cliente, id_funcionario, data_hora):
    if not (id_evento and id_cliente and id_funcionario):
        raise ValueError("Evento, cliente e funcionário são obrigatórios.")
    Agendamento(id_evento=id_evento,
                id_cliente=id_cliente,
                id_funcionario=id_funcionario,
                data_hora=data_hora).salvar()

def listar_agendamentos():
    return Agendamento.buscar_todos()
