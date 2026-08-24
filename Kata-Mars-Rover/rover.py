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
     
    def girar_izquierda(self):
        indice = self.direcciones_validas.index(self.direction)
        self.direction = self.direcciones_validas[(indice - 1) % 4]

    def girar_derecha(self):
        indice = self.direcciones_validas.index(self.direction)
        self.direction = self.direcciones_validas[(indice + 1) % 4]

    def mover_adelante(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'O':
            self.x -= 1
