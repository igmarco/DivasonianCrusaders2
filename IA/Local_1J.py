import sys
import time

from LN.Partida import Partida
from MD.Fichas.Arquero import Arquero
from MD.Fichas.Barbaro import Barbaro
from MD.Fichas.Caballero import Caballero
from MD.Fichas.Guerrero import Guerrero
from MD.Fichas.Lancero import Lancero
from MD.Instruccion.Operacion import Movimiento, Disparo
from Presentacion.Pintador import *

import sys
import os
import time
from datetime import datetime

import numpy as np

from IA.Node import Node, fromJSON, code, decode
from LN.Partida import Partida
from MD.Casillas.Catapulta import Catapulta
from MD.Instruccion.Operacion import Movimiento, Disparo
from Presentacion.Pintador import *
from Utilidades.Utilidades import Direccion

epsilon = 0.5

def Local_1J(nombreJ, nombreIA):

    print('Cargando...')
    IA1 = cargarIA(nombreIA)
    print('Cargado')
    nodoraiz1 = IA1

    rendicion1 = False
    partida = Partida()
    pintador = iniciarPintador(partida.tableroActual)

    print('Tablero del turno', partida.turno)
    print(partida.tableroActual)
    pintar(pintador, partida.tableroActual)

    while not partida.haTerminado:
        print('Comando del jugador:')
        time.sleep(0.001)
        comando1 = input()
        time.sleep(0.001)

        rendicion1 = comando1 == 'SURR'

        if rendicion1:
            if rendicion1:
                print("El jugador", nombreJ, "se ha rendido. Un tanto para,", nombreIA + ', otra inevitable victoria para las máquinas')
            break

        instruccion1 = procesarComando(comando1)
        instruccion2 = elegirInstruccion(partida, IA1)
        print(instruccion1)
        print(instruccion2)

        if code(instruccion1) in IA1.hijos:
            IA1 = IA1.get(code(instruccion1))
        else:
            IA1.insert(instruccion1, 0, 0)
            IA1 = IA1.get(code(instruccion1))

        codigoTablero = partida.tableroActual.codeTB()
        if codigoTablero in IA1.hijos:
            IA1 = IA1.get(codigoTablero)
        else:
            IA1.insert(codigoTablero, 0, 0)
            IA1 = IA1.get(code(codigoTablero))

        partida.ejecutarTurno(instruccion1, instruccion2)

        for ind, tablero in enumerate(partida.tablerosMovimientos):
            print('Tablero',ind, 'del turno', partida.turno)
            print(tablero)

            time.sleep(2)
            pintar(pintador, tablero)

        print('Tablero final del turno', partida.turno)
        print(partida.tableroActual)
        pintar(pintador, partida.tableroActual)

    if partida.tableroActual.getGanador() == 1:
        print('Enhorabuena, ha ganado', nombreJ, 'en el turno', partida.turno)
    if partida.tableroActual.getGanador() == 2:
        print('Enhorabuena, ha ganado', nombreIA, 'en el turno', partida.turno)
    elif partida.tableroActual.getGanador() == 0:
        print('Nada mal,', nombreJ, 'y', nombreIA, ', ha habido un empate en el turno', partida.turno)

        # Aquí toca hacer el back propagation.
        nodoBP = IA1
        if partida.tableroActual.getGanador() == 1:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 1 + (0.25 - partida.turno*0.005)
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 2:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins - 1 + (0.25 - partida.turno*0.005)
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 0:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 0 + (0.25 - partida.turno*0.005)
                nodoBP = nodoBP.padre

    guardarIA(nombreIA, nodoraiz1)

    print('Guardado')

    while (True):  # Esperar para cerrar la pantalla
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)  # salir del programa

def cargarIA(nombre):
    sys.setrecursionlimit(1500)

    contenido = os.listdir('saves')
    fichero = None
    for f in contenido:
        if f.split('_')[0] == 'IA' and nombre == f.split('_')[1] and (fichero is None or f.split('_')[2]>fichero.split('_')[2]):
            fichero = f
    if fichero is None:
        print('Error: Ninguna IA con ese nombre.')
        return None
    else:
        f = open('saves/' + fichero, 'r')
        return fromJSON(f.read())

def guardarIA(nombre, IA):
    f = open('saves/IA_'+nombre+'_'+"%s%03d" % (datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')[0], int(datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')[1]) / 1000)+'.txt', 'w')
    f.write(IA.toJSON())
    f.close()

def generarInstruccionAleatoria(tablero, faccion):
    instrElegida = []
    movimientos = {'Arquero':0,'Barbaro':0,'Caballero':0,'Guerrero':0,'Lancero':0}
    for i in range(6):
        fichasCatapulta = []
        if tablero.nodos[tablero.dondeEsta(Catapulta(1))].hayFicha(faccion):
            if tablero.nodos[tablero.dondeEsta(Catapulta(1))].fichaDefensora.faccion == faccion:
                fichasCatapulta.append(tablero.nodos[tablero.dondeEsta(Catapulta(1))].fichaDefensora)
            else:
                fichasCatapulta.append(tablero.nodos[tablero.dondeEsta(Catapulta(1))].fichaAtacante)
        if tablero.nodos[tablero.dondeEsta(Catapulta(2))].hayFicha(faccion):
            if tablero.nodos[tablero.dondeEsta(Catapulta(2))].fichaDefensora.faccion == faccion:
                fichasCatapulta.append(tablero.nodos[tablero.dondeEsta(Catapulta(2))].fichaDefensora)
            else:
                fichasCatapulta.append(tablero.nodos[tablero.dondeEsta(Catapulta(2))].fichaAtacante)
        if len(fichasCatapulta) > 0 and np.random.rand() > 0.8:
            if len(fichasCatapulta) == 2 and np.random.rand() > 0.5:
                listaPosTablero = tablero.dondeDispararProyectiles(
                    tablero.nodos[tablero.dondeEsta(fichasCatapulta[1])].casilla)
                posTablero = listaPosTablero[np.random.randint(len(listaPosTablero))]
                instrElegida.append(Disparo(fichasCatapulta[1], posTablero))
            else:
                listaPosTablero = tablero.dondeDispararProyectiles(
                    tablero.nodos[tablero.dondeEsta(fichasCatapulta[0])].casilla)
                posTablero = listaPosTablero[np.random.randint(len(listaPosTablero))]
                instrElegida.append(Disparo(fichasCatapulta[0], posTablero))
        else:
            if np.random.rand() > 0.5:
                listaFichasVivas = []
                for nodo in tablero.nodos:
                    if nodo.fichaDefensora is not None and nodo.fichaDefensora.faccion == faccion and nodo.fichaDefensora.puedeMover:
                        listaFichasVivas.append(nodo.fichaDefensora)
                    elif nodo.fichaAtacante is not None and nodo.fichaAtacante.faccion == faccion and nodo.fichaAtacante.puedeMover:
                        listaFichasVivas.append(nodo.fichaAtacante)
                if len(listaFichasVivas) == 0:
                    instrElegida.append(None)
                else:
                    fichaElegida = listaFichasVivas[np.random.randint(len(listaFichasVivas))]
                    listaPosTablero = tablero.dondePuedeMover(fichaElegida)
                    if len(listaPosTablero) == 0 or fichaElegida.getMovs() <= movimientos[type(fichaElegida).__name__]:
                        instrElegida.append(None)
                    else:
                        posTablero = listaPosTablero[np.random.randint(len(listaPosTablero))]
                        instrElegida.append(Movimiento(fichaElegida, Direccion[posTablero-tablero.dondeEsta(fichaElegida)]))
                        tablero.moverFichaDireccion(fichaElegida, Direccion[posTablero-tablero.dondeEsta(fichaElegida)])
                        movimientos[type(fichaElegida).__name__] += 1
            else:
                instrElegida.append(None)

    return instrElegida

def elegirInstruccion(partida, IA1):
    instruccion1 = []

    tableroPrueba1 = partida.tableroActual.copy()

    if IA1.ultimo:
        instruccion1 = generarInstruccionAleatoria(tableroPrueba1, 2)
    else:
        instrMejores = []
        mejorInstr = list(IA1.hijos.keys())[0]
        for instr in IA1.hijos:
            if IA1.puntuacion(mejorInstr, epsilon) < IA1.puntuacion(instr, epsilon):
                mejorInstr = instr
        if IA1.puntuacion(mejorInstr, epsilon) >= 0:
            for instr in IA1.hijos:
                if IA1.puntuacion(mejorInstr, epsilon) == IA1.puntuacion(instr, epsilon):
                    instrMejores.append(instr)
            instruccion1 = decode(instrMejores[np.random.randint(len(instrMejores))])
        else:
            existe = True
            while existe:
                instruccion1 = generarInstruccionAleatoria(tableroPrueba1, 2)
                if code(instruccion1) not in IA1.hijos:
                    existe = False

    return instruccion1

def procesarComando(comando1):

    comando1Splitted = comando1.replace(' ','').split(';')

    f1, o1 = None, None
    instruccion1 = []

    for opComando in comando1Splitted:
        opElementos = opComando.split(',')
        o1 = None

        if opElementos[0] == 'mover':
            if opElementos[1]=='lancero': f1 = Lancero(1)
            elif opElementos[1]=='guerrero': f1 = Guerrero(1)
            elif opElementos[1]=='arquero': f1 = Arquero(1)
            elif opElementos[1]=='barbaro': f1 = Barbaro(1)
            elif opElementos[1]=='caballero': f1 = Caballero(1)

            if opElementos[2]=='N': o1 = Movimiento(f1,0)
            elif opElementos[2]=='NE': o1 = Movimiento(f1,1)
            elif opElementos[2]=='E': o1 = Movimiento(f1,2)
            elif opElementos[2]=='SE': o1 = Movimiento(f1,3)
            elif opElementos[2]=='S': o1 = Movimiento(f1,4)
            elif opElementos[2]=='SW': o1 = Movimiento(f1,5)
            elif opElementos[2]=='W': o1 = Movimiento(f1,6)
            elif opElementos[2]=='NW': o1 = Movimiento(f1,7)

        elif opElementos[0] == 'disparar':
            if opElementos[1]=='lancero': f1 = Lancero(1)
            elif opElementos[1]=='guerrero': f1 = Guerrero(1)
            elif opElementos[1]=='arquero': f1 = Arquero(1)
            elif opElementos[1]=='barbaro': f1 = Barbaro(1)
            elif opElementos[1]=='caballero': f1 = Caballero(1)

            # o1 = Disparo(f1, int(opElementos[2]))
            o1 = Disparo(f1, x=int(opElementos[2]), y=int(opElementos[3]))

        instruccion1.append(o1)

    return instruccion1

IA1 = Node(0,0)
guardarIA('Nuevo', IA1)
Local_1J('Jugador 1', 'Nuevo')