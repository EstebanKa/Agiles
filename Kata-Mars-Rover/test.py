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

