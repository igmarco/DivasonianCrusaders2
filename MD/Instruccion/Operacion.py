from MD.Fichas.Arquero import Arquero
from MD.Fichas.Barbaro import Barbaro
from MD.Fichas.Caballero import Caballero
from MD.Fichas.Guerrero import Guerrero
from MD.Fichas.Lancero import Lancero


class Operacion:

    def __init__(self, ficha):
        self.ficha=ficha

    def __str__(self):
        return str(self.ficha)

    def code(self):
        return self.ficha.code()

class Movimiento(Operacion):

    def __init__(self, ficha, direccion):
        self.ficha = ficha
        self.direccion = direccion

    def __str__(self):
        return str(super) + ' mueve a ' + str(self.direccion)

    def code(self):
        return self.ficha.code() + ' M' + ' ' + str(self.direccion)

class Disparo(Operacion):

    def __init__(self, ficha, posTablero=None, x=None, y=None):
        self.ficha = ficha
        self.posTablero = posTablero
        if x is None and y is None:
            self.x, self.y = posTablero%9, 4-posTablero//9
        else:
            self.x, self.y = x, y
        if posTablero is None:
            self.posTablero = (4-y)*9+x

    def __str__(self):
        return str(super) + ' dispara a ' + str(self.posTablero)

    def code(self):
        return self.ficha.code() + ' D' + ' ' + str(self.posTablero)

def decodeOP(string):
    if string == '':
        return None
    strSplitted = string.split(' ')
    if strSplitted[0] == 'Arquero':
        ficha = Arquero(int(strSplitted[1]))
    elif strSplitted[0] == 'Barbaro':
        ficha = Barbaro(int(strSplitted[1]))
    elif strSplitted[0] == 'Caballero':
        ficha = Caballero(int(strSplitted[1]))
    elif strSplitted[0] == 'Guerrero':
        ficha = Guerrero(int(strSplitted[1]))
    elif strSplitted[0] == 'Lancero':
        ficha = Lancero(int(strSplitted[1]))
    if strSplitted[2] == 'M':
        return Movimiento(ficha,int(strSplitted[3]))
    elif strSplitted[2] == 'D':
        return Disparo(ficha,int(strSplitted[3]))