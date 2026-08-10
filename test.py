from calc import sumar

def test_vacio_igual_0():
    assert sumar("") == 0
    
def test_devolucion_mismo_numero():
    assert sumar("5") == 5

