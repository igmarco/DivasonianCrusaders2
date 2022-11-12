import numpy as np
import math as m

from MD.Casillas.Casilla import Casilla

class Catapulta(Casilla):

    def __init__(self, identificador, hachaDivasonica=None, danoProyectiles=15, danoProyectilesVariable=7, curacionAuxiliar=None):
        super().__init__(hachaDivasonica, False, curacionAuxiliar)
        self.danoProyectiles = danoProyectiles
        self.danoProyectilesVariable = danoProyectilesVariable
        self.identificador = identificador

    def realizarDisparo(self):
        return self.danoProyectiles + m.floor(np.random.rand() * 2 * self.danoProyectilesVariable - self.danoProyectilesVariable)

    def __eq__(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.identificador == self.identificador and casilla.identificador != 0

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Catapulta(self.identificador, hacha, self.danoProyectiles, self.danoProyectilesVariable, self.curacionAuxiliar)
