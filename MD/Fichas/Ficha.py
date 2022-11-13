import numpy as np
import math as m

from Utilidades.Utilidades import Faccion


class Ficha:

    def __init__(self, faccion, hachaDivasonica, dano=None, vida=None, vidaMaxima=None, danoVariable=None):
        self.dano = dano
        self.vida = vida
        self.vidaMaxima = vidaMaxima
        self.danoVariable = danoVariable
        self.hachaDivasonica = hachaDivasonica
        self.faccion = faccion

        self.movs = 2

        self.puedeMover = True

    def tieneHacha(self):
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
            self.vida = self.vida - self.hachaDivasonica.sufrirDanoPorTurno()

    def curarse(self,v):
        self.vida = self.vida + v if self.vida + v < self.vidaMaxima else self.vidaMaxima

    def __eq__(self,ficha):
        return ficha is not None and type(ficha) == type(self) and ficha.faccion == self.faccion

    def realizarCarga(self, ficha):
        return m.floor(self.realizarAtaque(ficha)*1.2)

    def realizarAtaqueContraHuida(self, ficha):
        return self.realizarCarga(ficha)/2

    def getMovs(self):
        return 2

    def __str__(self):
        if self.hachaDivasonica is not None:
            return type(self).__name__ + ', ' + Faccion[self.faccion] + ', ' + str(self.vida) + 'ps' + ' con Hacha'
        else:
            return type(self).__name__ + ', ' + Faccion[self.faccion] + ', ' + str(self.vida) + 'ps'

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Ficha(self.faccion, hacha, self.dano, self.vida, self.vidaMaxima, self.danoVariable)

    def code(self):
        return type(self).__name__ + ' ' + str(self.faccion)