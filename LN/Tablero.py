from MD.Casillas.Catapulta import Catapulta
from MD.Casillas.Colina import Colina
from MD.Casillas.Copa import Copa
from MD.Casillas.Curacion import Curacion
from MD.Casillas.Normal import Normal
from MD.Fichas.Arquero import Arquero
from MD.Fichas.Barbaro import Barbaro
from MD.Fichas.Caballero import Caballero
from MD.Fichas.Guerrero import Guerrero
from MD.Fichas.HachaDivasonica import HachaDivasonica
from MD.Fichas.Lancero import Lancero
from MD.Nodo.Nodo import Nodo
import random

from Utilidades.Utilidades import Direccion


class Tablero:

    def __init__(self, nodos = None):
        if nodos:
            self.nodos = nodos
        else:
            self.nodos = [Nodo() for i in range(45)]
            self.nodos[18], self.nodos[26] = Nodo(Copa(1)), Nodo(Copa(2))
            self.nodos[5], self.nodos[39] = Nodo(Colina()), Nodo(Colina())
            self.nodos[20], self.nodos[24] = Nodo(Catapulta(1)), Nodo(Catapulta(2))
            self.nodos[2], self.nodos[42] = Nodo(Curacion(1)), Nodo(Curacion(2))
            self.nodos[22] = Nodo(Normal(HachaDivasonica()))
            self.nodos[1], self.nodos[3], self.nodos[10], self.nodos[11], self.nodos[12] = \
                Nodo(Normal(casillaDeCuracion=True)), Nodo(Normal(casillaDeCuracion=True)), \
                Nodo(Normal(casillaDeCuracion=True)), Nodo(Normal(casillaDeCuracion=True)), Nodo(Normal(casillaDeCuracion=True))
            self.nodos[32], self.nodos[33], self.nodos[34], self.nodos[41], self.nodos[43] = \
                Nodo(Normal(casillaDeCuracion=True)), Nodo(Normal(casillaDeCuracion=True)), \
                Nodo(Normal(casillaDeCuracion=True)), Nodo(Normal(casillaDeCuracion=True)), Nodo(Normal(casillaDeCuracion=True))
            self.nodos[0] = Nodo(fichaDefensora=Lancero(1))
            self.nodos[8], self.nodos[9] = Nodo(fichaDefensora=Lancero(2)), Nodo(fichaDefensora=Arquero(1))
            self.nodos[17], self.nodos[19] = Nodo(fichaDefensora=Arquero(2)), Nodo(fichaDefensora=Guerrero(1))
            self.nodos[25], self.nodos[27] = Nodo(fichaDefensora=Guerrero(2)), Nodo(fichaDefensora=Barbaro(1))
            self.nodos[35], self.nodos[36] = Nodo(fichaDefensora=Barbaro(2)), Nodo(fichaDefensora=Caballero(1))
            self.nodos[44] = Nodo(fichaDefensora=Caballero(2))

    def movimientoPosible(self, ficha):
        pos = self.dondeEsta(ficha)
        return False if pos == -1 else self.nodos[pos].puedeMover(ficha)

    def estaTrabada(self, ficha):
        return self.hayDosFichas(self.dondeEsta(ficha))

    def moverFicha(self, ficha, casillaO, casillaDest):
        if self.nodos[casillaO].hayDosFichas():
            self.nodos[casillaO].ejecutarAtaqueContraHuida(ficha)
        if self.nodos[casillaO].estaAqui(ficha):
            freal = self.nodos[casillaO].quitarFicha(ficha)
            self.nodos[casillaDest].ponerFicha(freal)
            if self.nodos[casillaDest].hayDosFichas():
                self.nodos[casillaDest].ejecutarCarga()
                self.nodos[casillaDest].noPuedenMover()

    def moverDireccion(self, direccion, desde):
        if direccion == 0:
            hasta = desde - 9
        elif direccion == 4:
            hasta = desde + 9
        elif direccion == 2:
            hasta = desde + 1
        elif direccion == 6:
            hasta = desde - 1
        elif direccion == 1:
            hasta = desde - 8
        elif direccion == 7:
            hasta = desde - 10
        elif direccion == 3:
            hasta = desde + 10
        else:
            hasta = desde + 8
        return hasta

    def moverFichaDireccion(self, ficha, direccion):
        desde = self.dondeEsta(ficha)
        hasta = self.moverDireccion(direccion, desde)
        self.moverFicha(ficha, desde, hasta)


    def moverFichasALaVez(self, ficha1, dir1, ficha2, dir2):
        desde1 = self.dondeEsta(ficha1)
        hasta1 = self.moverDireccion(dir1, desde1)
        desde2 = self.dondeEsta(ficha2)
        hasta2 = self.moverDireccion(dir2, desde2)

        if desde1 == desde2:
            if hasta1 == hasta2:
                self.moverFichasDeLaMismaCasillaALaMismaCasilla(ficha1, ficha2, desde1, hasta1)
            else:
                self.moverFichasDeLaMismaCasilla(ficha1, ficha2, desde1, hasta1, hasta2)
        elif hasta1 == desde2:
            if hasta2 == desde1:
                self.cruzarFichas(ficha1, ficha2, desde1, desde2)
            else:
                self.moverFicha(ficha2, desde2, hasta2)
                self.moverFicha(ficha1, desde1, hasta1)
        elif hasta2 == desde1:
            self.moverFicha(ficha1, desde1, hasta1)
            self.moverFicha(ficha2, desde2, hasta2)
        elif hasta1 == hasta2:
            self.moverFichasALaMismaCasilla(ficha1, ficha2, desde1, desde2, hasta1)
        else:
            self.moverFicha(ficha1, desde1, hasta1)
            self.moverFicha(ficha2, desde2, hasta2)

    # Dale Pablo titán fuersa bro
    # Aquí, Pablo, gracias jefe.

    def moverFichasALaMismaCasilla(self, ficha1, ficha2,casO1, casO2, dest):
        if self.nodos[casO1].hayDosFichas():
            self.nodos[casO1].ejecutarAtaqueContraHuida(ficha1)
            self.nodos[casO2].ejecutarAtaqueContraHuida(ficha2)
        if self.nodos[casO2].hayDosFichas():
            self.nodos[casO2].ejecutarAtaqueContraHuida(ficha2)
        if self.nodos[casO1].estaAqui(ficha1) and self.nodos[casO2].estaAqui(ficha2):
            freal1 = self.nodos[casO1].quitarFicha(ficha1)
            freal2 = self.nodos[casO2].quitarFicha(ficha2)
            self.nodos[dest].ponerFicha(freal1)
            self.nodos[dest].ponerFicha(freal2)
            self.nodos[dest].ejecutarCargasRespectivas()
            self.nodos[dest].noPuedenMover()
        elif self.nodos[casO1].estaAqui(ficha1):
            freal1 = self.nodos[casO1].quitarFicha(ficha1)
            self.nodos[dest].ponerFicha(freal1)
        elif self.nodos[casO2].estaAqui(ficha2):
            freal2 = self.nodos[casO2].quitarFicha(ficha2)
            self.nodos[dest].ponerFicha(freal2)

    def moverFichasDeLaMismaCasilla(self, ficha1, ficha2, casillaO, casillaDest1, casillaDest2):
        self.nodos[casillaO].ejecutarAtaquesDeHuidas()
        if self.nodos[casillaO].estaAqui(ficha1):
            freal1 = self.nodos[casillaO].quitarFicha(ficha1)
            self.nodos[casillaDest1].ponerFicha(freal1)
            if self.nodos[casillaDest1].hayDosFichas():
                self.nodos[casillaDest1].ejecutarCarga()
                self.nodos[casillaDest1].noPuedenMover()
        if self.nodos[casillaO].estaAqui(ficha2):
            freal2 = self.nodos[casillaO].quitarFicha(ficha2)
            self.nodos[casillaDest2].ponerFicha(freal2)
            if self.nodos[casillaDest2].hayDosFichas():
                self.nodos[casillaDest2].ejecutarCarga()
                self.nodos[casillaDest2].noPuedenMover()


    def moverFichasDeLaMismaCasillaALaMismaCasilla(self, ficha1, ficha2, casillaO, casillaDest):
        self.nodos[casillaO].ejecutarAtaquesDeHuidas()
        if self.nodos[casillaO].estaAqui(ficha1):
            freal1 = self.nodos[casillaO].quitarFicha(ficha1)
            self.nodos[casillaDest].ponerFicha(freal1)
        if self.nodos[casillaO].estaAqui(ficha2):
            freal2 = self.nodos[casillaO].quitarFicha(ficha2)
            self.nodos[casillaDest].ponerFicha(freal2)

    def cruzarFichas(self, ficha1, ficha2, casillaO1, casillaO2):
        if  random.random() >= 0.5:
            self.moverFicha(ficha1, casillaO1, casillaO2)
            self.nodos[casillaO2].ejecutarCargasRespectivas()
            self.nodos[casillaO2].noPuedenMover()
        else:
            self.moverFicha(ficha2, casillaO2, casillaO1)
            self.nodos[casillaO1].ejecutarCargasRespectivas()
            self.nodos[casillaO1].noPuedenMover()

    def resolverTurno(self):
        dondeDispara1 = self.dondeDispararFlechas(1)
        dondeDispara2 = self.dondeDispararFlechas(2)
        for i, elem in enumerate(self.nodos):
            if i in dondeDispara1 and not elem.hayDosFichas() and elem.estaAqui(2):
                elem.recibirDisparo(self.nodos[self.dondeEsta(Arquero(1))].fichaDefensora.realizarDisparo())
            if i in dondeDispara2 and not elem.hayDosFichas() and elem.estaAqui(1):
                elem.recibirDisparo(self.nodos[self.dondeEsta(Arquero(2))].fichaDefensora.realizarDisparo())
            elem.resolverTurno()

    def haTerminado(self):
        posCopa1, posCopa2 = self.dondeEsta(Copa(1)), self.dondeEsta(Copa(2))
        algunoVivo1, algunoVivo2 = False, False

        if self.nodos[posCopa1].casilla.estaMuerta() or self.nodos[posCopa2].casilla.estaMuerta():
            return True

        for i in range(45):
            if self.nodos[i].estaAqui(1):
                algunoVivo1 = True
            if self.nodos[i].estaAqui(2):
                algunoVivo2 = True
        if not algunoVivo1 or not algunoVivo2:
            return True
        else:
            return False

    def getGanador(self):
        posCopa1, posCopa2 = self.dondeEsta(Copa(1)), self.dondeEsta(Copa(2))
        perdedor1, perdedor2 = False, False
        algunoVivo1, algunoVivo2 = False, False

        if self.nodos[posCopa1].casilla.estaMuerta():
            perdedor1 = True
        if self.nodos[posCopa2].casilla.estaMuerta():
            perdedor2 = True
        for i in range(45):
            if self.nodos[i].estaAqui(1): algunoVivo1 = True
            if self.nodos[i].estaAqui(2): algunoVivo2 = True
        if (perdedor1 or not algunoVivo1) and (perdedor2 or not algunoVivo2):
            return 0
        elif perdedor1 or not algunoVivo1:
            return 2
        elif perdedor2 or not algunoVivo2:
            return 1
        else:
            return None

    def dondeEsta(self, fichaOCasilla):
        donde = -1
        for i in range(45):
            if self.nodos[i].estaAqui(fichaOCasilla):
                donde = i
        return donde

    def dispararProyectiles(self, catapulta, x, y, ficha):
        cat = self.nodos[self.dondeEsta(catapulta)]
        casillaObjectivo = (4-y)*9 + x
        if ficha and ficha == cat.fichaDefensora and not cat.hayDosFichas():
            self.nodos[casillaObjectivo].recibirDisparo(catapulta.realizarDisparo())
            self.nodos[casillaObjectivo].cayoProyectil = True

    def hayFicha(self, casilla, faccion = None):
        return self.nodos[casilla].hayFicha(faccion) if faccion else self.nodos[casilla].hayFicha()

    def hayDosFichas(self, casilla):
        return self.nodos[casilla].hayDosFichas()

    def dondeDispararProyectiles(self, catapulta):
        posiciones = []
        if not catapulta:
            return posiciones
        if catapulta.identificador == 1:
            posiciones += [4,5,6,7,8,14,15,16,17,23,24,25,26,32,33,34,35,40,41,42,43,44]
        elif catapulta.identificador == 2:
            posiciones += [0, 1, 2, 3, 4, 9, 10, 11, 12, 18, 19, 20, 21, 27, 28, 29, 30, 36, 37, 38, 39, 40]
        return posiciones

    def catapultasQuePuedesDisparar(self, faccion):
        listaCasillas = []
        dondeCata1 = self.dondeEsta(Catapulta(1))
        dondeCata2 = self.dondeEsta(Catapulta(2))
        if self.nodos[dondeCata1].estaAqui(faccion) and not self.nodos[dondeCata1].hayDosFichas():
            listaCasillas.append(dondeCata1)
        if self.nodos[dondeCata2].estaAqui(faccion) and not self.nodos[dondeCata2].hayDosFichas():
            listaCasillas.append(dondeCata2)
        return listaCasillas

    def eliminarDeLista(self, lista, *valores):
        for valor in valores:
            if valor in lista:
                lista.remove(valor)

    def dondeDispararFlechas(self, faccion):
        posiciones = []
        dondeEstaArquero = self.dondeEsta(Arquero(faccion))
        if dondeEstaArquero == -1 or self.nodos[dondeEstaArquero].hayDosFichas():
            return posiciones
        posiciones.append(dondeEstaArquero -9 -1)
        posiciones.append(dondeEstaArquero - 9)
        posiciones.append(dondeEstaArquero - 9 + 1)
        posiciones.append(dondeEstaArquero - 1)
        posiciones.append(dondeEstaArquero + 1)
        posiciones.append(dondeEstaArquero + 9 - 1)
        posiciones.append(dondeEstaArquero + 9)
        posiciones.append(dondeEstaArquero + 9 + 1)
        if faccion == 1:
            posiciones.append(dondeEstaArquero - 9 - 2)
            posiciones.append(dondeEstaArquero + 2)
            posiciones.append(dondeEstaArquero + 9 + 2)
        elif faccion == 2:
            posiciones.append(dondeEstaArquero - 9 - 2)
            posiciones.append(dondeEstaArquero - 2)
            posiciones.append(dondeEstaArquero + 9 - 2)
        if dondeEstaArquero == 0:
            self.eliminarDeLista(posiciones, 8,7)
        elif dondeEstaArquero == 9:
            self.eliminarDeLista(posiciones, 8,7,17,16)
        elif dondeEstaArquero == 18:
            self.eliminarDeLista(posiciones, 17,26,8,16,25,7)
        elif dondeEstaArquero == 27:
            self.eliminarDeLista(posiciones, 26,35,17,25,34,16)
        elif dondeEstaArquero == 36:
            self.eliminarDeLista(posiciones, 35,44,34,43,26,25)
        elif dondeEstaArquero == 8:
            self.eliminarDeLista(posiciones, 0,1,9,10,18,19)
        elif dondeEstaArquero == 17:
            self.eliminarDeLista(posiciones, 27,28,9,10,18,19)
        elif dondeEstaArquero == 26:
            self.eliminarDeLista(posiciones, 36,37,18,19,27,28)
        elif dondeEstaArquero == 35:
            self.eliminarDeLista(posiciones, 27,28,36,37)
        elif dondeEstaArquero == 44:
            self.eliminarDeLista(posiciones, 36,37)

        fueraDeRango=[]
        for i in range(len(posiciones)):
            if posiciones[i] < 0 or posiciones[i] >= 45:
                # posiciones.remove(i)
                fueraDeRango.append(i)
        for i in fueraDeRango:
            posiciones.pop(i)
        return posiciones

    def dondePuedeMover(self, ficha):
        movPosibles = []
        dondeEsta = self.dondeEsta(ficha)

        if dondeEsta - 9 >= 0:
            movPosibles.append(dondeEsta - 9)
        if dondeEsta - 8 >= 0:
            movPosibles.append(dondeEsta - 8)
        if dondeEsta - 10 >= 0:
            movPosibles.append(dondeEsta - 10)
        if dondeEsta - 1 >= 0:
            movPosibles.append(dondeEsta - 1)
        if dondeEsta + 9 <= 45:
            movPosibles.append(dondeEsta + 9)
        if dondeEsta + 8 <= 45:
            movPosibles.append(dondeEsta + 8)
        if dondeEsta + 10 <= 45:
            movPosibles.append(dondeEsta + 10)
        if dondeEsta + 1 <= 45:
            movPosibles.append(dondeEsta + 1)

        if dondeEsta == 0:
            self.eliminarDeLista(movPosibles, 8)
        elif dondeEsta == 9:
            self.eliminarDeLista(movPosibles, 8,17)
        elif dondeEsta == 18:
            self.eliminarDeLista(movPosibles, 8,17,26)
        elif dondeEsta == 27:
            self.eliminarDeLista(movPosibles, 17,26,35)
        elif dondeEsta == 36:
            self.eliminarDeLista(movPosibles, 26,35,44)
        elif dondeEsta == 8:
            self.eliminarDeLista(movPosibles, 0,9,18)
        elif dondeEsta == 17:
            self.eliminarDeLista(movPosibles, 9,18,27)
        elif dondeEsta == 26:
            self.eliminarDeLista(movPosibles, 18,27,36)
        elif dondeEsta == 35:
            self.eliminarDeLista(movPosibles, 27,36)
        elif dondeEsta == 44:
            self.eliminarDeLista(movPosibles, 36)

        for i in movPosibles:
            if self.nodos[i].estaAqui(ficha.faccion) and i in movPosibles:
                movPosibles.remove(i)

        return movPosibles

    def quienesNOPuedenMover(self, faccion):
        movPisibles = []
        for i in range(45):
            if not self.nodos[i].estaAqui(faccion): movPisibles.append(i)
        return movPisibles

    def quienesPuedenMover(self, faccion):
        movPisibles = []
        for i in range(45):
            if self.nodos[i].estaAqui(faccion): movPisibles.append(i)
        return movPisibles

    def queFichaHay(self, faccion, casilla):
        if self.nodos[casilla].estaAqui(faccion):
            f = self.nodos[casilla].fichaDefensora.faccion
            return f if f == faccion else self.nodos[casilla].fichaAtacante
        else:
            return None

    def limpiarProyectiles(self):
        for elem in self.nodos:
            elem.cayoProyectil = False

    def copy(self):
        nodosCopiados = []
        for i in range(45):
            nodosCopiados.append(self.nodos[i].copy())
        return Tablero(nodosCopiados)

    def __str__(self):
        string = '===================================================\n'
        ind = 0
        for nodo in self.nodos:
            string = string + '[' + str(ind%9) + ', ' + str(4-ind//9) + '] - ' + str(nodo) + '\n'
            ind += 1
        return string + '===================================================\n'

# tablero = Tablero()
# print(tablero)
