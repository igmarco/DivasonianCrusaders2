import numpy as np
import math as m

from MD.Fichas.Ficha import Ficha

class Lancero (Ficha):

    def __init__(self, faccion=0, hachaDivasonica=None, dano=15, vida=125, vidaMaxima=125, danoVariable=5, danoACaballeria=35):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)
        self.danoACaballeria = danoACaballeria

    def realizarAtaque(self,ficha=None):
        hd = self.hachaDivasonica.sumarDano() if self.hachaDivasonica is not None else 0
        return self.danoACaballeria + m.floor(np.random.rand() * 2 * self.danoVariable - self.danoVariable) + hd if type(ficha).__name__ == 'Caballero' else self.dano + m.floor(np.random.rand() * 2 * self.danoVariable - self.danoVariable) + hd

    def copy(self):
        return Lancero(self.faccion, self.hachaDivasonica.copy(), self.dano, self.vida, self.vidaMaxima, self.danoVariable, self.danoACaballeria)