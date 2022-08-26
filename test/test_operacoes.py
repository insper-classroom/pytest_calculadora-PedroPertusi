import pytest
from matematica.Calculadora import *


@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1,v2)

@pytest.mark.op_simples
def test_soma_um_valor_positivos_um_negativo():
    assert 4 == soma(5,-1)

def test_subtrai_dois_valores_positivos():
    v1 = 7.0
    v2 = 5.0
    assert 2 == sub(v1,v2)

def test_multiplica_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1,v2)

def test_divide_dois_valores_positivos():
    v1 = 10.0
    v2 = 5.0
    assert 2 == divisao(v1,v2)

@pytest.mark.op_complexas
def test_media_lista_valores_positivos():
    l = [1,2,3,4,5]
    assert 3 == media_lista_valores(l)

@pytest.mark.exercicio_1
def test_divisao_por_zero():
    assert np.inf == divisao(10,0)

@pytest.mark.exercicio_1
def test_algo_dif_num_lista():
    assert 3 == media_lista_valores([1,2,3,'hello',4,5])

@pytest.mark.exercicio_1
def test_lista_vazia():
    assert 0 == media_lista_valores([])