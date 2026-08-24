from rover import Rover

def test_rover_initialization():
    rover = Rover(1, 0, 'N')
    assert rover.x == 1
    assert rover.y == 0
    assert rover.direction == 'N'

def test_rover_direccionL():
    rover = Rover(1, 0, 'L')
    assert rover.orientacion() == 'L'

def test_rover_direccionR():
    rover = Rover(1, 0, 'R')
    assert rover.orientacion() == 'R'

