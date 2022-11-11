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
            self.nodos = Nodo() * 45
            nodos[18], nodos[26] = Nodo(Copa(1)), Nodo(Copa(2))
            nodos[5], nodos[39] = Nodo(Colina()), Nodo(Colina())
            nodos[20], nodos[24] = Nodo(Catapulta(1)), Nodo(Catapulta(2))
            nodos[2], nodos[42] = Nodo(Curacion(1)), Nodo(Curacion(2))
            nodos[22] = Nodo(Normal(HachaDivasonica()))
            nodos[1], nodos[3], nodos[10:13] = Nodo(Normal()), Nodo(Normal()), Nodo(Normal())
            nodos[32:25], nodos[41], nodos[43] = Nodo(Normal()), Nodo(Normal()), Nodo(Normal())
            nodos[0], nodos[4], nodos[6:8] = Nodo(Lancero(1)), Nodo(), Nodo()
            nodos[8], nodos[9] = Nodo(Lancero(2)), Nodo(Arquero(1))
            nodos[17], nodos[19] = Nodo(Arquero(2)), Nodo(Guerrero(1))
            nodos[25], nodos[27] = Nodo(Guerrero(2)), Nodo(Barbaro(1))
            nodos[35], nodos[36] = Nodo(Barbaro(2)), Nodo(Caballero(1))
            nodos[44] = nodos(Caballero(2))

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
                self.nodos[casillaDest].ejecutarCrga()
                self.nodos[casillaDest].noPuedenMover()

    def moverDireccion(self, direccion, desde):
        if direccion == Direccion[0]:
            hasta = desde - 9
        elif direccion == Direccion[4]:
            hasta = desde + 9
        elif direccion == Direccion[2]:
            hasta = desde + 1
        elif direccion == Direccion[6]:
            hasta = desde - 1
        elif direccion == Direccion[1]:
            hasta = desde - 8
        elif direccion == Direccion[7]:
            hasta = desde - 10
        elif direccion == Direccion[3]:
            hasta = desde + 10
        else:
            hasta = desde + 8
        return hasta

    def moverFichaDireccion(self, ficha, direccion):
        desde = self.dondeEsta(ficha)
        hasta = self.moverDireccion(direccion, desde)
        if not self.hayFicha(hasta, ficha.getFaccion()):
            self.moverFicha(ficha, desde, hasta)
        else:
            self.nodos[self.dondeEsta(ficha)].getFicha(ficha).puedeMover = False


    def moverFichasALaVez(self, ficha1, dir1, ficha2, dir2):
        desde1 = self.dondeEsta(ficha1)
        hasta1 = self.moverDireccion(dir1, desde1)
        desde2 = self.dondeEsta(ficha2)
        hasta2 = self.moverDireccion(dir2, desde2)

        if desde1 == desde2 and hasta1 == hasta2:
            if not self.hayFicha(hasta1, ficha1.getFaccion()) and not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFichasDeLaMismaCasillaALaMismaCasilla(ficha1, ficha2, desde1, hasta1)
            elif not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
            elif not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFicha(ficha2, desde2, hasta2)
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
            else:
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
        if desde1 == desde2:
            if not self.hayFicha(hasta1, ficha1.getFaccion()) and not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFichasDeLaMismaCasilla(ficha1, ficha2, desde1, hasta1)
            elif not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
            elif not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFicha(ficha2, desde2, hasta2)
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
            else:
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
        elif hasta1 == desde2 and hasta2 == desde1:
            if not self.hayFicha(hasta1, ficha1.getFaccion()) and not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.cruzarFichas(ficha1, ficha2, desde1, desde2)
            elif not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
            elif not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFicha(ficha2, desde2, hasta2)
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
            else:
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
        elif hasta1 == desde2:
            if not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFicha(ficha2, desde2, hasta2)
            if not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
        elif hasta2 == desde1:
            if not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
            if not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFicha(ficha2, desde2, hasta2)
        elif hasta1 == hasta2:
            if not self.hayFicha(hasta1, ficha1.getFaccion()) and not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFichasALaMismaCasilla(ficha1, ficha2, desde1, desde2, hasta1)
            elif not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
            elif not self.hayFicha(hasta2, ficha2.getFaccion()):
                self.moverFicha(ficha2, desde2, hasta2)
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
            else:
                self.nodos[self.dondeEsta(ficha2)].getFicha(ficha2).puedeMover = False
                self.nodos[self.dondeEsta(ficha1)].getFicha(ficha1).puedeMover = False
        else:
            if not self.hayFicha(hasta1, ficha1.getFaccion()):
                self.moverFicha(ficha1, desde1, hasta1)
            if not self.hayFicha(hasta2, ficha2.getFaccion()):
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
            freal2 = self.nodos[casO2].quitarFicha(ficha2);
            self.nodos[dest].ponerFicha(freal1);
            self.nodos[dest].ponerFicha(freal2);
            self.nodos[dest].ejecutarCrgasRespectivas();
            self.nodos[dest].noPuedenMover();
        elif self.nodos[casO1].estaAqui(ficha1):
            freal1 = self.nodos[casO1].quitarFicha(ficha1)
            self.nodos[dest].ponerFicha(freal1);
        elif self.nodos[casO2].estaAqui(ficha2):
            freal2 = self.nodos[casO2].quitarFicha(ficha2)
            self.nodos[dest].ponerFicha(freal2);

    def moverFichasDeLaMismaCasilla(self, ficha1, ficha2, casillaO, casillaDest1, casillaDest2):
        self.nodos[casillaO].ejecutarAtaquesDeHuidas()
        if self.nodos[casillaO].estaAqui(ficha1):
            freal1 = self.nodos[casillaO].quitarFicha(ficha1)
            self.nodos[casillaDest1].ponerFicha(freal1)
            if self.nodos[casillaDest1].hayDosFichas():
                self.nodos[casillaDest1].ejecutarCrga()
                self.nodos[casillaDest1].noPuedenMover()
        if self.nodos[casillaO].estaAqui(ficha2):
            freal2 = self.nodos[casillaO].quitarFicha(ficha2)
            self.nodos[casillaDest2].ponerFicha(freal2)
            if self.nodos[casillaDest2].hayDosFichas():
                self.nodos[casillaDest2].ejecutarCrga()
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
            self.nodos[casillaO2].ejecutarCrgasRespectivas()
            self.nodos[casillaO2].noPuedenMover()
        else:
            self.moverFicha(ficha2, casillaO2, casillaO1)
            self.nodos[casillaO1].ejecutarCrgasRespectivas()
            self.nodos[casillaO1].noPuedenMover()

    def resolverTurno(self):
        dondeDispara1 = self.dondeDispararFlecha(1)
        dondeDispara2 = self.dondeDispararFlecha(2)
        for i, elem in enumerate(self.nodos):
            if i in dondeDispara1 and not elem.hayDosFichas() and elem.estaAqui(2):
                elem.recibirDisparo(self.nodos[self.dondeEsta(Arquero(1))].getFichaDefensora().realizarDisparo())
            if i in dondeDispara2 and not elem.hayDosFichas() and elem.estaAqui(1):
                elem.recibirDisparo(self.nodos[self.dondeEsta(Arquero(2))].getFichaDefensora().realizarDisparo())
            elem.resolverTurno()

    def haTerminado(self):
        posCopa1, posCopa2 = self.dondeEsta(Copa(1)), self.dondeEsta(Copa(2))
        algunoVivo1, algunoVivo2 = False, False

        if self.nodos[posCopa1].getCasilla().estaMuerta() or self.nodos[posCopa2].getCasilla().estaMuerta():
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

        if self.nodos[posCopa1].getCasilla().estaMuerta():
            perdedor1 = True
        if self.nodos[posCopa2].getCasilla().estaMuerta():
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

    def dondeEsta(self, ficha):
        for i in range(45):
            return  i if self.nodos[i].estaAqui(ficha) else -1

    def dispararProyectiles(self, catapulta, x, y, ficha):
        catPos = self.nodos[self.dondeEsta(catapulta)]
        casillaObjectivo = (4-y)*9 + x
        if ficha and ficha == self.nodos[catPos].getFichaDefensora() and not self.nodos[catPos].hayDosFichas():
            self.nodos[casillaObjectivo].recibirDisparo(catapulta.realizarDisparo())
            self.nodos[casillaObjectivo].carProyectil()

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
            posiciones.remove(8)
            posiciones.remove(7)
        elif dondeEstaArquero == 9:
            posiciones.remove(8)
            posiciones.remove(17)
            posiciones.remove(7)
            posiciones.remove(16)
        elif dondeEstaArquero == 18:
            posiciones.remove(17)
            posiciones.remove(26)
            posiciones.remove(8)
            posiciones.remove(16)
            posiciones.remove(7)
        elif dondeEstaArquero == 27:
            posiciones.remove(26)
            posiciones.remove(35)
            posiciones.remove(17)
            posiciones.remove(25)
            posiciones.remove(34)
            posiciones.remove(16)
        elif dondeEstaArquero == 36:
            posiciones.remove(35)
            posiciones.remove(44)
            posiciones.remove(34)
            posiciones.remove(43)
            posiciones.remove(26)
            posiciones.remove(25)
        elif dondeEstaArquero == 8:
            posiciones.remove(0)
            posiciones.remove(1)
            posiciones.remove(9)
            posiciones.remove(10)
            posiciones.remove(18)
            posiciones.remove(19)
        elif dondeEstaArquero == 17:
            posiciones.remove(27)
            posiciones.remove(28)
            posiciones.remove(9)
            posiciones.remove(10)
            posiciones.remove(18)
            posiciones.remove(19)
        elif dondeEstaArquero == 26:
            posiciones.remove(36)
            posiciones.remove(37)
            posiciones.remove(18)
            posiciones.remove(19)
            posiciones.remove(27)
            posiciones.remove(28)
        elif dondeEstaArquero == 35:
            posiciones.remove(27)
            posiciones.remove(28)
            posiciones.remove(36)
            posiciones.remove(37)
        elif dondeEstaArquero == 44:
            posiciones.remove(36)
            posiciones.remove(37)

        for i in range(len(posiciones)):
            if posiciones[i] < 0 or posiciones[i] >= 45:
                posiciones.remove(i)
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
            movPosibles.remove(8)
        elif dondeEsta == 9:
            movPosibles.remove(8)
            movPosibles.remove(17)
        elif dondeEsta == 18:
            movPosibles.remove(8)
            movPosibles.remove(17)
            movPosibles.remove(26)
        elif dondeEsta == 27:
            movPosibles.remove(17)
            movPosibles.remove(26)
            movPosibles.remove(35)
        elif dondeEsta == 36:
            movPosibles.remove(26)
            movPosibles.remove(35)
            movPosibles.remove(44)
        elif dondeEsta == 8:
            movPosibles.remove(0)
            movPosibles.remove(9)
            movPosibles.remove(18)
        elif dondeEsta == 17:
            movPosibles.remove(9)
            movPosibles.remove(18)
            movPosibles.remove(27)
        elif dondeEsta == 26:
            movPosibles.remove(18)
            movPosibles.remove(27)
            movPosibles.remove(36)
        elif dondeEsta == 35:
            movPosibles.remove(27)
            movPosibles.remove(36)
        elif dondeEsta == 44:
            movPosibles.remove(36)

        for i in movPosibles:
            if self.nodos[i].estaAqui(ficha.faccion):
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
            f = self.nodos[casilla].getFichaDefensora().getFaccion
            return f if f == faccion else self.nodos[casilla].getFichaAtacante()
        else:
            return None

    def getNodo(self, i):
       return self.nodos[i]

    def limpiarProyectiles(self):
        map(elem.limpiarProyectil() for elem in self.nodos)

    # def getFromElemento(self, elemento):
    #     #TODO:

    def copy(self):
        nodosCopiados = []
        for i in range(45):
            nodosCopiados.append(self.nodos[i].copy())
        return Tablero(nodosCopiados)

