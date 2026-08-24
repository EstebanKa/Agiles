from rover import Rover

def test_rover_initialization():
    rover = Rover(0, 0, 'N')
    assert rover.x == 0
    assert rover.y == 0
    assert rover.direction == 'N'