import pytest
import numpy as np
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
import requests

@pytest.mark.teste_classe_PessoaFisica
def test_name_type_int():
    with pytest.raises(TypeError) as exc:
        nome_int = 12
        pessoa = PessoaFisica(nome=nome_int)
    assert 'TypeError' in str(exc)

@pytest.mark.teste_classe_PessoaFisica
def test_name_type_str():
    nome = 'Carlos'
    pessoa = PessoaFisica(nome=nome)
    assert nome == pessoa.nome 

@pytest.mark.teste_classe_PessoaFisica
def test_cpf_type_float():
    with pytest.raises(TypeError) as exc:
        cpf = 12.0
        pessoa = PessoaFisica(cpf=cpf)
    assert 'TypeError' in str(exc)

@pytest.mark.teste_classe_PessoaFisica
def test_lista_sem_pessoas():
    lista = PessoaFisica.busca_nome('Renato Aragão')
    assert 'Nenhum usuário com este nome!' == lista

@pytest.mark.teste_classe_PessoaFisica_erros_corrigidos
def test_deleta_endereco_inexistente():
    with pytest.raises(KeyError) as exc:
        end = Endereco(86010630, 1078)
        pessoa = PessoaFisica('Eduardo')
        pessoa.adicionar_endereco('casa',end)

        pessoa.remover_endereco('trabalho')
    assert 'KeyError' in str(exc)