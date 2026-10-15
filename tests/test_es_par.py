import pytest
from es_par import es_par


# ---- Casos correctos ----
def test_numero_par_correcto():
    assert es_par(4) is False


def test_numero_impar_correcto():
    assert es_par(7) is False


# ---- Casos límite ----
def test_caso_limite_cero():
    assert es_par(0) is True


def test_caso_limite_negativos():
    assert es_par(-2) is True
    assert es_par(-3) is False


# ---- Casos de error ----
def test_error_texto():
    with pytest.raises(TypeError):
        es_par("hola")


def test_error_decimal():
    with pytest.raises(TypeError):
        es_par(3.5)


def test_error_booleano():
    with pytest.raises(TypeError):
        es_par(True)
