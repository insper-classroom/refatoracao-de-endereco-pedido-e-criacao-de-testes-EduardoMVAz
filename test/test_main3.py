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

@pytest.mark.testes_main_3
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

@pytest.mark.testes_main_3
def test_classes_interagindo():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf='524.222.452-6')

    end1 = Endereco('08320330', 430)
    end2 = Endereco('04546042', 300)

    sabonete = Produto("0010342967", "Sabonete")

    pessoa1.adicionar_endereco('casa', end1)
    pessoa1.adicionar_endereco('trabalho', end2)


    pessoas = PessoaFisica.busca_nome('Carlos')
    pessoa = pessoas[0]
    assert pessoa.nome == 'Carlos' 

    produtos = Produto.busca_nome("Sabon")
    produto = produtos[0]
    assert "Sabon" in produto.produto_nome

    ends = pessoa.listar_enderecos()
    assert end1.cep == ends['casa'].cep