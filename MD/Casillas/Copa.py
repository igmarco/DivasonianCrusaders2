from MD.Casillas.Casilla import Casilla

class Copa(Casilla):

    def __init__(self, hachaDivasonica, faccion, vida):
        self.faccion = faccion
        self.vida = vida

    def sufrirDano(self,dano):
        self.vida = self.vida - dano

    def estaMuerta(self):
        return self.vida <= 0

    def equals(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.faccion == self.faccion