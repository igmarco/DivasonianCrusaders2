import numpy as np
import math as m

from MD.Fichas.Ficha import Ficha

class Caballero (Ficha):

    def __init__(self, faccion, hachaDivasonica=None, dano=20, vida=100, vidaMaxima=100, danoVariable=10, danoCarga=30):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)
        self.danoCarga = danoCarga

        self.movs = 2

    def realizarCarga(self, ficha):
        hd = self.hachaDivasonica.sumarDano() if self.hachaDivasonica is not None else 0
        return m.floor(self.danoCarga + m.floor(np.random.rand()*2*self.danoVariable - self.danoVariable + hd)*1.2)

    def copy(self):
        return Caballero(self.faccion, self.hachaDivasonica.copy(), self.dano, self.vida, self.vidaMaxima, self.danoVariable, self.danoCarga)