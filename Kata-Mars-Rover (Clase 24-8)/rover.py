class Rover:

    direcciones_validas = ['N', 'E', 'S', 'O']
    DELTAS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # mismo orden que direcciones_validas

    #Paso 1: El rover informa su posición y orientación iniciales
    def __init__(self, x, y, direction, obstaculos=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.obstaculos = obstaculos or []

    # Paso 2: Gira a la izquierda. Gira a la derecha
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

    # Paso 3: Avanza una celda
    def mover_adelante(self):
        dx, dy = self.DELTAS[self.direcciones_validas.index(self.direction)]
        self.x += dx
        self.y += dy

    #Cambio requerimiento: Salta dos celdas hacia adelante, pero si hay un obstáculo en la celda de destino, no se mueve
    def saltar(self):
        dx, dy = self.DELTAS[self.direcciones_validas.index(self.direction)]
        destino = (self.x + dx * 2, self.y + dy * 2)
        if destino in self.obstaculos:
            return  # choca, no se mueve
        self.x, self.y = destino
