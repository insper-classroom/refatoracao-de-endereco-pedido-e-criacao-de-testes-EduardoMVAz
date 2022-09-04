import pytest
import numpy as np
from classes.Endereco import Endereco
import requests

@pytest.mark.teste_classe_Endereco
def test_no_values():
    with pytest.raises(TypeError) as exc:
        end = Endereco()

    assert 'missing 2 required positional arguments' in str(exc.value)

@pytest.mark.teste_classe_Endereco
def test_no_nmbr():
    with pytest.raises(TypeError) as exc:
        end = Endereco(cep='86010630')

    assert "missing 1 required positional argument: 'numero'" in str(exc.value)

@pytest.mark.teste_classe_Endereco
def test_no_cep():
    with pytest.raises(TypeError) as exc:
        end = Endereco(numero=1078)

    assert "missing 1 required positional argument: 'cep'" in str(exc.value)

@pytest.mark.teste_classe_Endereco
def test_cep_as_int_or_str():
    cep = 86010630
    nmr = 1078
    end = Endereco(cep=cep,numero=nmr)
    if type(end.cep) == str:
        assert end.cep == str(cep)
    elif type(end.cep) == int:
        assert end.cep == cep

@pytest.mark.teste_classe_Endereco
def test_cep_as_float():
    with pytest.raises(TypeError) as exc:
        cep = 86010630.0
        nmr = 1078.0
        end = Endereco(cep=cep,numero=nmr)
    assert 'TypeError' in str(exc)

@pytest.mark.teste_funcao_consultar_cep
def test_unexistent_cep():
    with pytest.raises(KeyError) as exc:
        cep = 99999999
        nmr = 1078
        end = Endereco(cep=cep,numero=nmr)
    assert 'KeyError' in str(exc)

@pytest.mark.teste_funcao_consultar_cep
def test_no_connection():
    with pytest.raises(requests.exceptions.ConnectionError) as exc:
        cep = 86010630
        nmr = 1078
        end = Endereco(cep=cep,numero=nmr)
    assert 'ConnectionError' in str(exc)

@pytest.mark.teste_funcao_consultar_cep
def test_wrong_cep_format():
    with pytest.raises(TypeError) as exc:
        cep = 9
        nmr = 10
        end = Endereco(cep=cep,numero=nmr)
    assert "'bool' object is not subscriptable" in str(exc)