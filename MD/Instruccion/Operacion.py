class Operacion:

    def __init__(self, ficha):
        self.ficha=ficha

    def __str__(self):
        return str(self.ficha)

class Movimiento(Operacion):

    def __init__(self, ficha, direccion):
        self.ficha = ficha
        self.direccion = direccion

    def __str__(self):
        return str(super) + ' mueve a ' + str(self.direccion)

class Disparo(Operacion):

    def __init__(self, ficha, posTablero=None, x=None, y=None):
        self.ficha = ficha
        self.posTablero = posTablero
        if x is None and y is None:
            self.x, self.y = posTablero%9, 4-posTablero//9
        else:
            self.x, self.y = x, y

    def __str__(self):
        return str(super) + ' dispara a ' + str(self.posTablero)