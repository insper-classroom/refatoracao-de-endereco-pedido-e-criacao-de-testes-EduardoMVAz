import pytest
import numpy as np
from classes.Pedido import Pedido
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
from classes.Produto import Produto
import requests

@pytest.mark.teste_classe_Pedido
def test_cria_pedido_com_cliente():
    carrinho = Carrinho()
    pessoa = PessoaFisica('Eduardo')

    pedido = Pedido(pessoa, carrinho)
    assert pedido.cliente == pessoa

@pytest.mark.teste_classe_Pedido
def test_cria_pedido_com_carrinho_e_produtos():
    carrinho = Carrinho()
    pessoa = PessoaFisica('Eduardo')

    nome = 'Sabonete'
    id = 150015
    produto = Produto(id,nome)
    carrinho.adicionar_item(produto, 10)

    assert 10 == carrinho.itens[produto]