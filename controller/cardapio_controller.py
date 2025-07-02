from models.cardapio_model import Cardapio

def cadastrar_item(nome_item, descricao_item):
    if not nome_item:
        raise ValueError("O nome do item é obrigatório.")

    item = Cardapio(nome_item=nome_item, descricao_item=descricao_item)
    item.salvar()

def listar_itens():
    return Cardapio.buscar_todos()
