import numpy as np
import math as m

class Casilla ():

    def __init__(self,hachaDivasonica=None, casillaDeCuracion=False, curacionAuxiliar=None):
        self.hachaDivasonica = hachaDivasonica
        if casillaDeCuracion:
            self.curacionAuxiliar = 5
        elif curacionAuxiliar is not None:
            self.curacionAuxiliar = curacionAuxiliar
        else:
            self.curacionAuxiliar = 0

    def __eq__(self,casilla):
        return casilla is not None and type(casilla) == type(self)

    def tieneHacha(self):
        return self.hachaDivasonica is not None

    def casillaDeCura(self):
        return self.curacionAuxiliar != 0

    def __str__(self):
        if self.hachaDivasonica is not None:
            return type(self).__name__ + ' con Hacha'
        else:
            return type(self).__name__

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Casilla(hacha, self.casillaDeCuracion, self.curacionAuxiliar)