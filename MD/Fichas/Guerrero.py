from MD.Fichas.Ficha import Ficha

class Guerrero (Ficha):

    def __init__(self, faccion, hachaDivasonica=None, dano=18, vida=150, vidaMaxima=150, danoVariable=2):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)