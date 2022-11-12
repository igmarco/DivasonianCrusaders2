from MD.Fichas.Ficha import Ficha

class Barbaro (Ficha):

    def __init__(self, faccion=0, hachaDivasonica=None, dano=30, vida=100, vidaMaxima=100, danoVariable=15):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Barbaro(self.faccion, hacha, self.dano, self.vida, self.vidaMaxima, self.danoVariable)