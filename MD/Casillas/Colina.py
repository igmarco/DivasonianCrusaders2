from MD.Casillas.Casilla import Casilla

class Colina(Casilla):

    def __init__(self, hachaDivasonica, curacionAuxiliar=None, danoExtra=10):
        super().__init__(hachaDivasonica, False, curacionAuxiliar)
        self.danoExtra = danoExtra