import pytest
import numpy as np
from classes.Carrinho import Carrinho
from classes.Produto import Produto
import requests

@pytest.mark.teste_classe_Carrinho
def test_adiciona_produto_sem_qtd():
    nome = 'Sabonete'
    id = 150015
    produto = Produto(id,nome)

    carrinho = Carrinho()
    carrinho.adicionar_item(produto)
    assert 1 == carrinho.itens[produto]

@pytest.mark.teste_classe_Carrinho
def test_qtd_formato_errado():
    with pytest.raises(TypeError) as exc:
        nome = 'Sabonete'
        id = 150015
        produto = Produto(id,nome)

        carrinho = Carrinho()
        carrinho.adicionar_item(produto, 'olá denovo tiago')
    assert 'TypeError' in str(exc)

@pytest.mark.teste_classe_Carrinho
def test_tenta_alterar_produto_inexistente():
    carrinho = Carrinho()
    resultado = carrinho.altera_quantidade('olá miranda', 17689)
    assert 'Esse Item não existe!' == resultado

@pytest.mark.teste_classe_Carrinho
def test_tenta_deletar_produto_inexistente():
    carrinho = Carrinho()
    resultado = carrinho.remover_item('olá denovo miranda! gostando da aps?')
    assert 'Esse Item não existe!' == resultado