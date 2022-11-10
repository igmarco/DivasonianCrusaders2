from MD.Casillas.Casilla import Casilla

class Copa(Casilla):

    def __init__(self, hachaDivasonica, faccion=0, vida=5):
        super().__init__(hachaDivasonica, False, None)
        self.faccion = faccion
        self.vida = vida

    def sufrirDano(self,dano):
        self.vida = self.vida - dano

    def estaMuerta(self):
        return self.vida <= 0

    def __eq__(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.faccion == self.faccion