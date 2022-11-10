class Operacion:

    def __init__(self, ficha):
        self.ficha=ficha

    def __str__(self):
        return str(self.ficha)

class Movimiento(Operacion):

    def __init__(self, ficha, direccion):
        self.direccion = direccion

    def __str__(self):
        return str(super) + ' mueve a ' + str(self.direccion)

class Disparo(Operacion):

    def __init__(self, ficha, catapulta, posTablero):
        self.catapulta = catapulta
        self.posTablero = posTablero

    def __str__(self):
        return str(super) + ' dispara a ' + str(self.posTablero)