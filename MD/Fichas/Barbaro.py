from MD.Fichas.Ficha import Ficha

class Barbaro (Ficha):

    def __init__(self, faccion, hachaDivasonica=None, dano=30, vida=100, vidaMaxima=100, danoVariable=15):
        super().__init__(faccion, hachaDivasonica, dano, vida, vidaMaxima, danoVariable)