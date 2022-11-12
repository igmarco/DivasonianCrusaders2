from MD.Casillas.Casilla import Casilla

class Copa(Casilla):

    def __init__(self, faccion=0, hachaDivasonica=None, vida=50):
        super().__init__(hachaDivasonica, False, None)
        self.faccion = faccion
        self.vida = vida

    def __str__(self):
        if self.hachaDivasonica is not None:
            return type(self).__name__ + ' ' + str(self.vida) + 'ps ' + ' con Hacha'
        else:
            return type(self).__name__

    def sufrirDano(self,dano):
        self.vida = self.vida - dano

    def estaMuerta(self):
        return self.vida <= 0

    def __eq__(self,casilla):
        return casilla is not None and type(casilla) == type(self) and casilla.faccion == self.faccion

    def copy(self):
        hacha = self.hachaDivasonica.copy() if self.hachaDivasonica else None
        return Copa(self.faccion, hacha, self.vida)