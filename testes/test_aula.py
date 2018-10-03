import pytest
from .models import Calculadora

def test_soma():
    assert Calculadora().soma(2, 2) == 4
    assert Calculadora().soma(1, -1) == 0

def test_subtracao():
    assert Calculadora().subtrai(1, 1) == 0
    assert Calculadora().subtrai(1, 2) == -1
    assert Calculadora().subtrai(-1, 1) == 0

def test_multiplicacao():
	assert Calculadora().multiplica(10, 2) == 20
	assert Calculadora().multiplica(10, 1) == 10

def test_divisao():
    assert Calculadora().divide(10,0) == 0
    assert Calculadora().divide(10,2) == 5