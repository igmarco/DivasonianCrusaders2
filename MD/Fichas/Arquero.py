import numpy as np
import math as m

from MD.Fichas.Ficha import Ficha

class Arquero (Ficha):

    def __init__(self,faccion, dano=10, vida=75, vidaMaxima=75, danoVariable=3, hachaDivasonica=None, danoFlechas=10, danoflechasvariable=5):
        self.danoFlechas = danoFlechas
        self.danoFlechasVariable = danoflechasvariable

    def realizarDisparo(self):
        return self.danoFlechas + m.floor(np.random.rand()*2*self.danoFlechasVariable - self.danoFlechasVariable)
