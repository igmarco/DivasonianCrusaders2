class Operacion:

    def __init__(self, ficha):
        self.ficha=ficha

class Disparo(Operacion):

    def __init__(self, ficha, direccion):
        self.direccion = direccion

class Movimiento(Operacion):

    def __init__(self, ficha, catapulta, posTablero):
        self.catapulta = catapulta
        self.posTablero = posTablero