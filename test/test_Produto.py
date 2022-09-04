import pytest
import numpy as np
from classes.Produto import Produto
import requests

@pytest.mark.teste_classe_Produto
def test_name_type_str():
    nome = 'Sabonete'
    id = 150015
    produto = Produto(id,nome)
    assert nome == produto.produto_nome

@pytest.mark.teste_classe_Produto
def test_name_type_int():
    with pytest.raises(TypeError) as exc:
        nome = 1234567890
        id = 150015
        produto = Produto(id,nome)
    assert 'TypeError' in str(exc)

@pytest.mark.teste_classe_Produto
def test_tenta_trocar_id_para_invalido():
    with pytest.raises(TypeError) as exc:
        nome = 'Sabonete'
        id = 150015
        produto = Produto(id,nome)

        produto.set_id('new_id')
    assert 'TypeError' in str(exc)

@pytest.mark.teste_classe_Produto
def test_get_id():
    nome = 'Sabonete'
    id = 150015
    produto = Produto(id,nome)

    id_teste = produto.get_id()
    assert id_teste == id

@pytest.mark.teste_classe_Produto
def test_lista_sem_produtos():
    tentativa_de_lista = Produto.busca_nome('Tiagão!')
    assert 'Esse produto não existe!' == tentativa_de_lista

    