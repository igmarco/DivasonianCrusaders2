from MD.Casillas.Casilla import Casilla

class Normal(Casilla):

    def __init__(self, hachaDivasonica=None, casillaDeCuracion=None, curacionAuxiliar=None):
        super().__init__(hachaDivasonica, casillaDeCuracion, curacionAuxiliar)

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Normal(hacha, curacionAuxiliar=self.curacionAuxiliar)