import numpy as np
import math as m

from MD.Fichas.Ficha import Ficha

class Arquero (Ficha):

    def __init__(self,faccion, hachaDivasonica=None, dano=10, vida=75, vidaMaxima=75, danoVariable=3, danoFlechas=10, danoflechasvariable=5):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)
        self.danoFlechas = danoFlechas
        self.danoFlechasVariable = danoflechasvariable

    def realizarDisparo(self):
        return self.danoFlechas + m.floor(np.random.rand()*2*self.danoFlechasVariable - self.danoFlechasVariable)

    def copy(self):
        return Arquero(self.faccion, self.hachaDivasonica.copy(), self.dano, self.vida, self.vidaMaxima, self.danoVariable, self.danoFlechas, self.danoflechasvariable)
