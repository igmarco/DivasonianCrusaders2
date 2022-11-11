from MD.Fichas.Ficha import Ficha

class Guerrero (Ficha):

    def __init__(self, faccion=0, hachaDivasonica=None, dano=18, vida=150, vidaMaxima=150, danoVariable=2):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)

    def copy(self):
        return Guerrero(self.faccion, self.hachaDivasonica.copy(), self.dano, self.vida, self.vidaMaxima, self.danoVariable)