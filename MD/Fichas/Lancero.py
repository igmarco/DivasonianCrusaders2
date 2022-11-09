import numpy as np
import math as m

from MD.Fichas.Ficha import Ficha

class Lancero (Ficha):

    def __init__(self, faccion, dano=15, vida=125, vidaMaxima=125, danoVariable=5, hachaDivasonica=None, danoACaballeria=35):
        self.danoACaballeria = danoACaballeria

    def realizarAtaque(self,ficha):
        hd = self.hachaDivasonica.sumarDano() if self.hachaDivasonica is not None else 0
        return self.danoACaballería + m.floor(np.random.rand()*2*(self.danoVariable)-self.danoVariable) + hd if type(ficha).__name__ == 'Caballero' else self.dano + m.floor(np.random.rand()*2*(self.danoVariable)-self.danoVariable) + hd
