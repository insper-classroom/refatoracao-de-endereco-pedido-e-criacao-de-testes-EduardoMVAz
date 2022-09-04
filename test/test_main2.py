from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco
from classes.Pedido import Pedido
from classes.Produto import Produto
from classes.Carrinho import Carrinho
from classes.Pagamentos import Pagamento

import pytest
import numpy as np
import requests
import copy

@pytest.mark.testes_main_2
def test_inicializa_classes():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf='524.222.452-6')
    assert pessoa1.nome == 'Carlos'

    end1 = Endereco('08320330', 430)
    end2 = Endereco('04546042', 300)

    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)

    assert pessoa1.enderecos['casa'] == end1
    assert pessoa1.enderecos['trabalho'] == end2

    sabonete = Produto("0010342967", "Sabonete")
    assert sabonete.produto_id == "0010342967"
    assert sabonete.produto_nome == "Sabonete"

@pytest.mark.testes_main_2
def test_classes_interagindo():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf='524.222.452-6')

    end1 = Endereco('08320330', 430)
    end2 = Endereco('04546042', 300)

    sabonete = Produto("0010342967", "Sabonete")

    carrinho = Carrinho()
    carrinho.adicionar_item(sabonete, 10)
    assert carrinho.itens[sabonete] == 10

    pedido = Pedido(pessoa1, carrinho)
    assert pedido.cliente == pessoa1
    assert pedido.carrinho == carrinho

    pedido.endereco_entrega = copy.deepcopy(end1) 
    pedido.endereco_faturamento = copy.deepcopy(end2)

    assert pedido.endereco_entrega.cep == '08320330'
    assert pedido.endereco_faturamento.cep == '04546042'