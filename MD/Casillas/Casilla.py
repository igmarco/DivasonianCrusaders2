import numpy as np
import math as m

class Casilla ():

    def __init__(self,hachaDivasonica=None, casillaDeCura=None, curacionAuxiliar=None):
        self.hachaDivasonica = hachaDivasonica;
        if casillaDeCura:
            self.curacionAuxiliar = 5
        elif curacionAuxiliar is not None:
            self.curacionAuxiliar = curacionAuxiliar
        else:
            self.curacionAuxiliar = 0

    def equals(self,casilla):
        return casilla is not None and type(casilla) == type(self)

    def tieneHacha(self):
        return self.hachaDivasonica is not None

    def casillaDeCura(self):
        return self.curacionAuxiliar != 0