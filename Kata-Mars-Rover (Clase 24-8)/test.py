from rover import Rover

def test_rover_initialization():
    rover = Rover(1, 0, 'N')
    assert rover.x == 1
    assert rover.y == 0
    assert rover.direction == 'N'

def test_rover_gira_izquierda():
    rover = Rover(1, 0, 'N')
    rover.girar_izquierda()
    assert rover.orientacion() == 'O'

def test_rover_gira_derecha():
    rover = Rover(1, 0, 'N')
    rover.girar_derecha()
    assert rover.orientacion() == 'E'

def test_rover_mueve_hacia_adelante():
    rover = Rover(1, 0, 'N')
    rover.mover_adelante()
    assert rover.posicion() == (1, 1)

def test_rover_salta_hacia_el_norte():
    rover = Rover(1, 0, 'N')
    rover.saltar()
    assert rover.posicion() == (1, 2)

def test_rover_no_salta_si_hay_obstaculo():
    rover = Rover(1, 0, 'N', obstaculos=[(1, 2)])
    rover.saltar()
    assert rover.posicion() == (1, 0)  # no se movió, "chocó"