# controllers/funcionario_controller.py
from models.funcionario_model import Funcionario

def cadastrar_funcionario(nome, email, cargo):
    if not nome:
        raise ValueError("O nome do funcionário é obrigatório.")
    Funcionario(nome=nome, email=email, cargo=cargo).salvar()

def listar_funcionarios():
    return Funcionario.buscar_todos()
