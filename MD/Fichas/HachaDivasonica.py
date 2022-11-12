import numpy as np
import math as m

class HachaDivasonica ():

    def __init__(self, danoExtra=10, danoExtraVariable=7, vidaPorTurno=5, vidaPorTurnoVariable=4):
        self.danoExtra = danoExtra
        self.danoExtraVariable = danoExtraVariable
        self.vidaPorTurno = vidaPorTurno
        self.vidaPorTurnoVariable = vidaPorTurnoVariable

    def sumarDano(self):
        return self.danoExtra + m.floor(np.random.rand() * 2 * self.danoExtraVariable - 1)

    def sufrirDanoPorTurno(self):
        return self.vidaPorTurno + m.floor(np.random.rand()*2*self.vidaPorTurnoVariable-1)

    def copy(self):
        return HachaDivasonica(self.danoExtra, self.danoExtraVariable, self.vidaPorTurno, self.vidaPorTurnoVariable)

