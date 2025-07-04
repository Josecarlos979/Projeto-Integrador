# controllers/evento_controller.py
from models.evento_model import Evento

def cadastrar_evento(titulo, descricao, data):
    if not titulo:
        raise ValueError("O título do evento é obrigatório.")
    Evento(titulo=titulo, descricao=descricao, data=data).salvar()

def listar_eventos():
    return Evento.buscar_todos()
