"""
Camada intermediária entre View e Model.
Regra de negócio simples: nome é obrigatório.
"""
from models.cardapio_model import Cardapio


def cadastrar_item(nome_item: str, descricao_item: str | None):
    nome_item = (nome_item or "").strip()
    descricao_item = (descricao_item or "").strip()

    if not nome_item:
        raise ValueError("O nome do item é obrigatório.")

    item = Cardapio(nome_item=nome_item, descricao_item=descricao_item)
    item.salvar()


def listar_itens():
    return Cardapio.buscar_todos()
