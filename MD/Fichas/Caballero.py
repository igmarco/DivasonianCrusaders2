import numpy as np
import math as m

from MD.Fichas.Ficha import Ficha

class Caballero (Ficha):

    def __init__(self, faccion, dano=20, vida=100, vidaMaxima=100, danoVariable=10, hachaDivasonica=None, danoCarga=30):
        self.danoCarga = danoCarga

    def realizarCarga(self, ficha):
        hd = self.hachaDivasonica.sumarDano() if self.hachaDivasonica is not None else 0
        return m.floor(self.danoCarga + m.floor(np.random.rand()*2*self.danoVariable - self.danoVariable + hd)*1.2)

    def getMovs(self):
        return 3