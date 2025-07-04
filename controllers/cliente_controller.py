# controllers/cliente_controller.py
from models.cliente_model import Cliente

def cadastrar_cliente(nome, email, telefone):
    if not nome:
        raise ValueError("O nome do cliente é obrigatório.")
    Cliente(nome=nome, email=email, telefone=telefone).salvar()

def listar_clientes():
    return Cliente.buscar_todos()

