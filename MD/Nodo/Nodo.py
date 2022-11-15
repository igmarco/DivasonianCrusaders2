from MD.Casillas.Normal import *

class Nodo():

    def __init__(self, casilla=None, fichaDefensora=None, fichaAtacante=None, cayoProyectil=False):
        self.casilla = casilla if casilla is not None else Normal()
        self.fichaDefensora=fichaDefensora
        self.fichaAtacante=fichaAtacante
        self.cayoProyectil=cayoProyectil

    def __str__(self):
        string = str(self.casilla)
        if self.fichaDefensora is not None:
            string += ': ' + str(self.fichaDefensora)
            if self.fichaAtacante is not None:
                string += ' VS. ' + str(self.fichaAtacante)
        if self.cayoProyectil:
            string += ' con proyectil'
        return string

    def estaAqui(self,fichaOCasillaOFaccion):
        if fichaOCasillaOFaccion is None:
            return False
        elif fichaOCasillaOFaccion == self.casilla or fichaOCasillaOFaccion == self.fichaDefensora or \
                fichaOCasillaOFaccion == self.fichaAtacante or (self.fichaDefensora and fichaOCasillaOFaccion == self.fichaDefensora.faccion) \
                or (self.fichaAtacante and fichaOCasillaOFaccion == self.fichaAtacante.faccion):
            return True

    def ponerFicha(self,ficha):
        if self.fichaDefensora is None:
            self.fichaDefensora = ficha
        else:
            self.fichaAtacante = ficha

    def quitarFicha(self,ficha):
        if ficha is None:
            return None
        freturn = None
        if self.fichaDefensora == ficha:
            freturn = self.fichaDefensora
            self.fichaDefensora = self.fichaAtacante
            self.fichaAtacante = None
        elif self.fichaAtacante == ficha:
            freturn = self.fichaAtacante
            if self.fichaAtacante is not None:
                self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarAtaque(self.fichaDefensora))
            self.fichaAtacante = None
        return freturn

    def resolverTurno(self):
        self.resolverCombate()
        self.darCuracion()
        self.sufrirHacha()
        self.sufrirCorrupcionRomeriana()

        self.comprobarMuertes()

        if self.fichaAtacante is not None:
            self.fichaAtacante.puedeMover = True
        if self.fichaDefensora is not None:
            self.fichaDefensora.puedeMover = True

        if self.casilla.tieneHacha() and self.fichaDefensora is not None and self.fichaAtacante is None:
            self.fichaDefensora.hachaDivasonica = self.casilla.hachaDivasonica
            self.casilla.hachaDivasonica = None

        # if self.casilla.tieneHacha() and self.fichaDefensora is not None and self.fichaAtacante is None and self.fichaDefensora.hachaDivasonica is None:
        # 	self.fichaDefensora.hachaDivasonica = self.casilla.hachaDivasonica

        if type(self.casilla).__name__ == 'Copa' and self.fichaDefensora is not None and self.fichaAtacante is None and self.fichaDefensora.faccion != self.casilla.faccion:
            self.casilla.sufrirDano(self.fichaDefensora.realizarAtaque())

    def resolverCombate(self):
        if self.fichaDefensora is not None and self.fichaAtacante is not None:
            self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarAtaque(self.fichaDefensora))
            self.fichaAtacante.sufrirDano(self.fichaDefensora.realizarAtaque(self.fichaAtacante))

    def darCuracion(self):
        if type(self.casilla).__name__ == 'Curacion':
            if self.fichaDefensora is not None:
                self.fichaDefensora.curarse(self.casilla.curar() + self.casilla.curacionAuxiliar)
            if self.fichaAtacante is not None:
                self.fichaAtacante.curarse(self.casilla.curar() + self.casilla.curacionAuxiliar)
        else:
            if self.fichaDefensora is not None:
                self.fichaDefensora.curarse(self.casilla.curacionAuxiliar)
            if self.fichaAtacante is not None:
                self.fichaAtacante.curarse(self.casilla.curacionAuxiliar)

    def sufrirHacha(self):
        if self.fichaDefensora is not None:
            self.fichaDefensora.sufrirHacha()
        if self.fichaAtacante is not None:
            self.fichaAtacante.sufrirHacha()

    def sufrirCorrupcionRomeriana(self):
        if self.fichaDefensora is not None:
            self.fichaDefensora.sufrirCorrupcionRomeriana()
        if self.fichaAtacante is not None:
            self.fichaAtacante.sufrirCorrupcionRomeriana()

    def recibirDisparo(self, dano):
        if self.fichaDefensora is not None:
            self.fichaDefensora.sufrirDano(dano)
        if self.fichaAtacante is not None:
            self.fichaAtacante.sufrirDano(dano)

        self.comprobarMuertes()

    def hayFicha(self, faccion=None):
        if faccion:
            return (self.fichaDefensora is not None and self.fichaDefensora.faccion == faccion) or (self.fichaAtacante is not None and self.fichaAtacante.faccion == faccion)
        else:
            return self.fichaDefensora is not None

    def hayDosFichas(self):
        return self.fichaAtacante is not None

    def ejecutarCarga(self):
        self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarCarga(self.fichaDefensora))

        if type(self.casilla).__name__ == 'Colina':
            self.fichaAtacante.sufrirDano((self.fichaDefensora.realizarAtaque(self.fichaAtacante)) + self.casilla.danoExtra)
        else:
            self.fichaAtacante.sufrirDano(self.fichaDefensora.realizarAtaque(self.fichaAtacante))

        self.comprobarMuertes()

    def ejecutarCargasRespectivas(self):


        self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarAtaqueContraHuida(self.fichaDefensora))
        self.fichaAtacante.sufrirDano(self.fichaDefensora.realizarAtaqueContraHuida(self.fichaAtacante))

        self.comprobarMuertes()

    def ejecutarAtaqueContraHuida(self, fichaCobarde):
        if fichaCobarde is not None:
            if fichaCobarde == self.fichaDefensora:
                self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarAtaqueContraHuida(self.fichaDefensora))
            elif fichaCobarde == self.fichaAtacante:
                self.fichaAtacante.sufrirDano(self.fichaDefensora.realizarAtaqueContraHuida(self.fichaAtacante))

    def ejecutarAtaquesDeHuidas(self):
        if self.hayDosFichas():
            self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarCarga(self.fichaDefensora))
            self.fichaAtacante.sufrirDano(self.fichaDefensora.realizarCarga(self.fichaAtacante))

        self.comprobarMuertes()

    def comprobarMuertes(self):
        if self.fichaAtacante is not None and self.fichaAtacante.estaMuerta():
            if self.fichaAtacante.tieneHacha() and not self.fichaDefensora.tieneHacha():
                self.fichaDefensora.hachaDivasonica = self.fichaAtacante.hachaDivasonica
            self.fichaAtacante = None

        if self.fichaDefensora is not None and self.fichaDefensora.estaMuerta():
            if self.fichaDefensora.tieneHacha():
                if self.fichaAtacante is not None and not self.fichaAtacante.tieneHacha():
                    self.fichaAtacante.hachaDivasonica = self.fichaDefensora.hachaDivasonica
                elif not self.casilla.tieneHacha():
                    self.casilla.hachaDivasonica = self.fichaDefensora.hachaDivasonica
            self.fichaDefensora = self.fichaAtacante
            self.fichaAtacante = None

    def noPuedeMover(self, ficha):
        if ficha is not None:
            if ficha == self.fichaDefensora:
                self.fichaDefensora.puedeMover = False
            elif ficha == self.fichaAtacante:
                self.fichaAtacante.puedeMover = False

    def noPuedenMover(self):
        if self.fichaDefensora is not None:
            self.fichaDefensora.puedeMover = False
        if self.fichaAtacante is not None:
            self.fichaAtacante.puedeMover = False

    def puedeMover(self, ficha):
        if ficha is None:
            return False
        if ficha == self.fichaDefensora:
            return self.fichaDefensora.puedeMover
        if ficha == self.fichaAtacante:
            return self.fichaAtacante.puedeMover

    def copy(self):
        casilla = self.casilla.copy() if self.casilla else None
        fichaDefensora = self.fichaDefensora.copy() if self.fichaDefensora else None
        fichaAtacante = self.fichaAtacante.copy() if self.fichaAtacante else None
        return Nodo(casilla, fichaDefensora, fichaAtacante, self.cayoProyectil)