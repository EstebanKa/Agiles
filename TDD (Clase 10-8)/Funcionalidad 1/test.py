from calc import sumar

def test_vacio_igual_0():
    assert sumar("") == 0
    
def test_devolucion_mismo_numero():
    assert sumar("5") == 5

def test_debe_sumar_dos_numeros():
    assert sumar("1,2") == 3