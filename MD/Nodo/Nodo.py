from MD.Casillas.Normal import *

class Nodo():

    def __init__(self, casilla=None, fichaDefensora=None, fichaAtacante=None, cayoProyectil=False):
        self.casilla = casilla if casilla is not None else Normal()
        self.fichaDefensora=fichaDefensora
        self.fichaAtacante=fichaAtacante
        self.cayoProyectil=cayoProyectil

    def estaAqui(self,fichaOCasillaOFaccion):
        if fichaOCasillaOFaccion is None:
            return False
        elif fichaOCasillaOFaccion.equals(self.casilla) or fichaOCasillaOFaccion.equals(self.fichaDefensora) or \
                fichaOCasillaOFaccion.equals(self.fichaAtacante) or fichaOCasillaOFaccion==self.fichaDefensora.faccion \
                or fichaOCasillaOFaccion == self.fichaAtacante.faccion:
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
        if self.fichaDefensora.equals(ficha):
            freturn = self.fichaDefensora
            self.fichaDefensora = self.fichaAtacante
            self.fichaAtacante = None
        elif self.fichaAtacante.equals(ficha):
            freturn = self.fichaAtacante
            if self.fichaAtacante is not None:
                self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarAtaque(self.fichaDefensora))
            self.fichaAtacante = None
        return freturn

    def resolverTurno(self):
        self.resolverCombate()
        self.darCuracion()
        self.sufrirHacha()

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

    def sufrirHacha(self):
        if self.fichaDefensora is not None:
            self.fichaDefensora.sufrirHacha()
        if self.fichaAtacante is not None:
            self.fichaAtacante.sufrirHacha()

    def recibirDisparo(self, dano):
        if self.fichaDefensora is not None:
            self.fichaDefensora.sufrirDano(dano)
        if self.fichaAtacante is not None:
            self.fichaAtacante.sufrirDano(dano)

        self.comprobarMuertes()

    def hayFicha(self):
        return self.fichaDefensora is not None

    def hayDosFichas(self):
        return self.fichaAtacante is not None

    def ejecutarCarga(self):
        self.fichaDefensora.sufrirDano(self.fichaAtacante.realizarCarga(self.fichaDefensora))

        if type(self.casilla).__none__ == 'Colina':
            self.fichaAtacante.sufrirDano((self.fichaDefensora.realizarAtaque(self.fichaAtacante)) + self.casilla.getDanoExtra())
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
        if self.hayDosFifhas():
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
        return Nodo(self.casilla.copy(), self.fichaDefensora.copy(), self.fichaAtacante.copy(), self.cayoProyectil)