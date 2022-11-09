import numpy as np
import math as m

class Ficha:

    def __init__(self, faccion, dano, vida, vidaMaxima, danoVariable, hachaDivasonica):
        self.dano = dano
        self.vida = vida
        self.vidaMaxima = vidaMaxima
        self.danoVariable = danoVariable
        self.hachaDivasonica = hachaDivasonica
        self.faccion = faccion

        self.puedeMover = True

    def tieneHachaDivasonica(self):
        return self.hachaDivasonica is not None

    def realizarAtaque(self,ficha=None):
        hd = self.hachaDivasonica.sumarDano() if self.hachaDivasonica is not None else 0
        return self.dano + m.floor(np.random.rand()*2*self.danoVariable - self.danoVariable) + hd

    def sufrirDano(self,dano):
        self.vida = self.vida - dano

    def estaMuerta(self):
        return self.vida <= 0

    def sufrirHacha(self):
        if self.hachaDivasonica is not None:
            self.vida = self.vida - self.hachaDivasonica.sufrirDano()

    def curarse(self,v):
        self.vida = self.vida + v if self.vida + v < self.vidaMaxima else self.vidaMaxima

    def equals(self,ficha):
        return ficha is not None and ficha.faccion == self.faccion and type(ficha) == type(self)

    def realizarCarga(self, ficha):
        return m.floor(self.realizarAtaque(ficha)*1.2)

    def realizarAtaqueContraHuida(self, ficha):
        return self.realizarCarga(ficha)/2

    def getMovs(self):
        return 2