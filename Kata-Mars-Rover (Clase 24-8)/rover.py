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

    #Paso 3 con cambio de requerimiento adaptado: Mueve hacia adelante y salta hacia adelante, pero no puede saltar si hay un obstáculo en la posición de destino.
    def _mover(self, pasos):
        dx, dy = self.DELTAS[self.direcciones_validas.index(self.direction)]
        destino = (self.x + dx * pasos, self.y + dy * pasos)
        if destino in self.obstaculos:
            return
        self.x, self.y = destino

    def mover_adelante(self):
        self._mover(1)

    def saltar(self):
        self._mover(2)

    #Paso 4: Retrocede una celda (requerimiento incorporado)
    def retroceder(self):
        self._mover(-1)
