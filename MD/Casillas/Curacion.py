import numpy as np
import math as m

from MD.Casillas.Casilla import Casilla

class Curacion(Casilla):

    def __init__(self, hachaDivasonica, curacion, curacionVariable, identificador):
        self.curacion = curacion
        self.curacionVariable = curacionVariable
        self.identificador = identificador

    def curar(self):
        return self.curacion + m.floor(np.random.rand()*2*self.curacionVariable-1)

    def equals(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.identificador() == self.identificador and casilla.identificador() != 0