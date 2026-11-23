import pytest
from altavoz import Altavoz


# Creación del altavoz

def test_guardar_nombre():
    altavoz = Altavoz("Salón", 30)
    assert altavoz.nombre == "Salón"


def test_guardar_volumen():
    altavoz = Altavoz("Salón", 30)
    assert altavoz.volumen == 30


def test_estado_inicial():
    altavoz = Altavoz("Salón", 30)
    assert altavoz.estado == "apagado"


# Propiedades

def test_quitar_espacios_del_nombre():
    altavoz = Altavoz("  Cocina  ", 30)
    assert altavoz.nombre == "Cocina"


def test_cambiar_nombre():
    altavoz = Altavoz("Salón", 30)
    altavoz.nombre = "Dormitorio"
    assert altavoz.nombre == "Dormitorio"


def test_quitar_espacios_al_cambiar_nombre():
    altavoz = Altavoz("Salón", 30)
    altavoz.nombre = "  Cocina  "
    assert altavoz.nombre == "Cocina"


def test_cambiar_volumen():
    altavoz = Altavoz("Salón", 30)
    altavoz.volumen = 50
    assert altavoz.volumen == 50


def test_volumen_minimo():
    altavoz = Altavoz("Salón", 0)
    assert altavoz.volumen == 0


def test_volumen_maximo():
    altavoz = Altavoz("Salón", 100)
    assert altavoz.volumen == 100


def test_encender_dos_veces():
    altavoz = Altavoz("Salón", 30)
    altavoz.encender()
    altavoz.encender()
    assert altavoz.estado == "encendido"


def test_no_cambiar_estado_directamente():
    altavoz = Altavoz("Salón", 30)
    with pytest.raises(AttributeError):
        altavoz.estado = "encendido"
        


# Encender y apagar

def test_encender():
    altavoz = Altavoz("Salón", 30)
    altavoz.encender()
    assert altavoz.estado == "encendido"


def test_apagar():
    altavoz = Altavoz("Salón", 30)
    altavoz.apagar()
    assert altavoz.estado == "apagado"


def test_encender_y_apagar():
    altavoz = Altavoz("Salón", 30)
    altavoz.encender()
    altavoz.apagar()
    assert altavoz.estado == "apagado"


# Datos incorrectos

def test_nombre_vacio():
    with pytest.raises(ValueError):
        Altavoz("", 30)


def test_nombre_con_espacios():
    with pytest.raises(ValueError):
        Altavoz("   ", 30)


def test_nombre_con_numero():
    with pytest.raises(ValueError):
        Altavoz(25, 30)


def test_cambiar_nombre_a_vacio():
    altavoz = Altavoz("Salón", 30)
    with pytest.raises(ValueError):
        altavoz.nombre = ""


def test_volumen_negativo():
    with pytest.raises(ValueError):
        Altavoz("Salón", -1)


def test_volumen_superior_a_100():
    with pytest.raises(ValueError):
        Altavoz("Salón", 101)


def test_volumen_con_texto():
    with pytest.raises(ValueError):
        Altavoz("Salón", "50")


def test_volumen_booleano():
    with pytest.raises(ValueError):
        Altavoz("Salón", True)


def test_cambiar_volumen_a_decimal():
    altavoz = Altavoz("Salón", 30)
    with pytest.raises(ValueError):
        altavoz.volumen = 25.5


def test_cambiar_volumen_a_texto():
    altavoz = Altavoz("Salón", 30)
    with pytest.raises(ValueError):
        altavoz.volumen = "alto"
