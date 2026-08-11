from calc import sumar

def test_vacio_igual_0():
    assert sumar("") == 0
    
def test_devolucion_mismo_numero():
    assert sumar("5") == 5

def test_suma_dos_numeros_separados_por_coma():
    assert sumar("1,2") == 3

def test_suma_multiples_numeros_separados_por_coma():
    assert sumar("1,2,3") == 6

def test_suma_seis_numeros_separados_por_coma():
    assert sumar("1,2,3,5,8,13") == 32