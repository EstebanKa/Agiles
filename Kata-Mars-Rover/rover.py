class Rover:

    direcciones_validas = ['N', 'E', 'S', 'O']
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def posicion(self):
        return (self.x, self.y)

    def orientacion(self):
        return self.direction