from MD.Casillas.Casilla import Casilla

class Colina(Casilla):

    def __init__(self, hachaDivasonica=None, curacionAuxiliar=None, danoExtra=10):
        super().__init__(hachaDivasonica, False, curacionAuxiliar)
        self.danoExtra = danoExtra

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Colina(hacha, self.curacionAuxiliar, self.danoExtra)