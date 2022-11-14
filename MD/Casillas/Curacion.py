import numpy as np
import math as m

from MD.Casillas.Casilla import Casilla

class Curacion(Casilla):

    def __init__(self, identificador=0, hachaDivasonica=None, curacion=10, curacionVariable=5):
        super().__init__(hachaDivasonica, False, None)
        self.curacion = curacion
        self.curacionVariable = curacionVariable
        self.identificador = identificador

    def curar(self):
        return self.curacion + m.floor(np.random.rand()*2*self.curacionVariable-1)

    def __eq__(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.identificador == self.identificador and casilla.identificador != 0

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica is not None else None
        return Curacion(self.identificador, hacha, self.curacion, self.curacionVariable)