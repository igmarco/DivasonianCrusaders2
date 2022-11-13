import sys
from datetime import datetime
import os

import numpy as np

from IA.Node import Node, fromJSON, code
from LN.Partida import Partida
from MD.Casillas.Catapulta import Catapulta
from MD.Fichas.Arquero import Arquero
from MD.Fichas.Barbaro import Barbaro
from MD.Fichas.Caballero import Caballero
from MD.Fichas.Guerrero import Guerrero
from MD.Fichas.Lancero import Lancero
from MD.Instruccion.Operacion import Movimiento, Disparo
from Presentacion.Pintador import *

epsilon = 0.5

def cargarIA(nombre):
    contenido = os.listdir('saves')
    fichero = None
    for f in contenido:
        if nombre in f and (fichero is None or f.split('_')[2]>fichero.split('_')[2]):
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

# root = Node(0,1)
# root.insert([Movimiento(Arquero(1),0),None,None,None,None,Disparo(Guerrero(1),x=7,y=2)],1,3)
# root.insert([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=1,y=3)],2,2)
# root.get([Movimiento(Arquero(1),0),None,None,None,None,Disparo(Guerrero(1),x=7,y=2)]).insert([Movimiento(Arquero(1),6),None,None,None,None,Disparo(Guerrero(1),x=2,y=3)],3,5)
# root.get([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=1,y=3)]).insert([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=3,y=3)],4,7)
# root.get([Movimiento(Arquero(1),0),None,None,None,None,Disparo(Guerrero(1),x=7,y=2)]).get([Movimiento(Arquero(1),6),None,None,None,None,Disparo(Guerrero(1),x=2,y=3)]).insert([Movimiento(Arquero(1),6),None,None,None,None,Disparo(Guerrero(1),x=4,y=3)],5,5)
# root.get([Movimiento(Arquero(1),0),None,None,None,None,Disparo(Guerrero(1),x=7,y=2)]).get([Movimiento(Arquero(1),6),None,None,None,None,Disparo(Guerrero(1),x=2,y=3)]).insert([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=5,y=3)],6,7)
# root.get([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=1,y=3)]).get([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=3,y=3)]).insert([Movimiento(Arquero(1),6),None,None,None,None,Disparo(Guerrero(1),x=6,y=3)],7,8)
# root.get([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=1,y=3)]).get([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=3,y=3)]).insert([Movimiento(Arquero(2),6),None,None,None,None,Disparo(Guerrero(2),x=7,y=3)],8,12)
# print(root)
# guardarIA('Prueba',root)
# IA = cargarIA('Prueba')
# print(IA)

def entrenarIAs(nombre1, nombre2, partidas=100):
    IA1 = cargarIA(nombre1)
    IA2 = cargarIA(nombre2)

    if IA1 is None or IA2 is None:
        print('Error al cargar las IAs')
    else:
        entrenar(IA1, IA2, nombre1, nombre2, partidas)

def entrenar(IA1, IA2, nombre1, nombre2, partidas):
    for i in range(partidas):
        partida = Partida()
        pintador = iniciarPintador(partida.tableroActual)

        print('Tablero del turno', partida.turno)
        print(partida.tableroActual)
        pintar(pintador, partida.tableroActual)

        while not partida.haTerminado:
            instruccion1, instruccion2 = elegirInstrucciones(IA1, IA2, partida)
            IA1 = IA1.get(instruccion1.code())
            IA2 = IA2.get(instruccion2.code())

            partida.ejecutarTurno(instruccion1, instruccion2)

            # for ind, tablero in enumerate(partida.tablerosMovimientos):
            #     print('Tablero',ind, 'del turno', partida.turno)
            #     print(tablero)
            #
            #     time.sleep(2)
            #     pintar(pintador, tablero)

            print('Tablero final del turno', partida.turno)
            print(partida.tableroActual)
            pintar(pintador, partida.tableroActual)

        if partida.tableroActual.getGanador() == 1:
            print('Enhorabuena, ha ganado', nombre1, 'en el turno', partida.turno)
        if partida.tableroActual.getGanador() == 2:
            print('Enhorabuena, ha ganado', nombre2, 'en el turno', partida.turno)
        elif partida.tableroActual.getGanador() == 0:
            print('Nada mal,', nombre1, 'y', nombre2, ', ha habido un empate en el turno', partida.turno)

        #Aquí toca hacer el back propagation.
        nodoBP = IA1
        if partida.tableroActual.getGanador() == 1:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 1
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 2:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins - 1
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 0:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 0
                nodoBP = nodoBP.padre

        nodoBP = IA2
        if partida.tableroActual.getGanador() == 2:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 1
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 1:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins - 1
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 0:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 0
                nodoBP = nodoBP.padre

    while (True):  # Esperar para cerrar la pantalla
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)  # salir del programa

def generarInstruccionAleatoria(tablero, faccion):
    instrElegida = []
    for i in range(6):
        fichasCatapulta = []
        if tablero[tablero.dondeEsta(Catapulta(1))].hayFicha(faccion):
            if tablero[tablero.dondeEsta(Catapulta(1))].fichaDefensora.faccion == faccion:
                fichasCatapulta.append(tablero[tablero.dondeEsta(Catapulta(1))].fichaDefensora)
            else:
                fichasCatapulta.append(tablero[tablero.dondeEsta(Catapulta(1))].fichaAtacante)
        if tablero[tablero.dondeEsta(Catapulta(2))].hayFicha(faccion):
            if tablero[tablero.dondeEsta(Catapulta(2))].fichaDefensora.faccion == faccion:
                fichasCatapulta.append(tablero[tablero.dondeEsta(Catapulta(2))].fichaDefensora)
            else:
                fichasCatapulta.append(tablero[tablero.dondeEsta(Catapulta(2))].fichaAtacante)
        if len(fichasCatapulta) > 0 and np.random.rand() > 0.8:
            if len(fichasCatapulta) == 2 and np.random.rand() > 0.5:
                listaPosTablero = tablero.dondeDispararProyectiles(
                    tablero[tablero.dondeEsta(fichasCatapulta[1])].casilla)
                posTablero = listaPosTablero[np.random.randint(0, len(listaPosTablero))]
                instrElegida.append(Disparo(fichasCatapulta[1], posTablero))
            else:
                listaPosTablero = tablero.dondeDispararProyectiles(
                    tablero[tablero.dondeEsta(fichasCatapulta[0])].casilla)
                posTablero = listaPosTablero[np.random.randint(0, len(listaPosTablero))]
                instrElegida.append(Disparo(fichasCatapulta[0], posTablero))
        else:
            if np.random.rand() > 0.5:
                listaFichasVivas = []
                for nodo in tablero.nodos:
                    if nodo.fichaDefensora.faccion == faccion and nodo.fichaDefensora.puedeMover:
                        listaFichasVivas.append(nodo.fichaDefensora)
                    elif nodo.fichaAtacante.faccion == faccion and nodo.fichaAtacante.puedeMover:
                        listaFichasVivas.append(nodo.fichaAtacante)
                fichaElegida = listaFichasVivas[np.random.randint(0, len(listaFichasVivas))]
                listaPosTablero = tablero.dondePuedeMover(fichaElegida)
                posTablero = listaPosTablero[np.random.randint(0, len(listaPosTablero))]
                instrElegida.append(Movimiento(fichaElegida, posTablero))
            else:
                instrElegida.append(None)

    return instrElegida

def elegirInstrucciones(IA1, IA2, partida):
    instruccion1, instruccion2 = [], []

    tableroPrueba1 = partida.tableroActual.copy()
    tableroPrueba2 = partida.tableroActual.copy()

    if IA1.ultimo:
        instruccion1 = generarInstruccionAleatoria(tableroPrueba1, 1)
    else:
        instrMejores = []
        mejorInstr = IA1.hijos[0]
        for instr in IA1.hijos:
            if IA1.getPuntuacion(mejorInstr,epsilon) < IA1.getPuntuacion(instr,epsilon):
                mejorInstr = instr
        if IA1.getPuntuacion(mejorInstr, epsilon) > 0:
            for instr in IA1.hijos:
                if IA1.getPuntuacion(mejorInstr, epsilon) == IA1.getPuntuacion(instr, epsilon):
                    instrMejores.append(instr)
            instruccion1 = instrMejores[np.random.randint(0, len(instrMejores))]
        else:
            existe = True
            while existe:
                instruccion1 = generarInstruccionAleatoria(tableroPrueba1, 1)
                if code(instruccion1) not in IA1.hijos:
                    existe = False

    if IA2.ultimo:
        instruccion2 = generarInstruccionAleatoria(tableroPrueba2, 2)
    else:
        instrMejores = []
        mejorInstr = IA2.hijos[0]
        for instr in IA2.hijos:
            if IA2.getPuntuacion(mejorInstr,epsilon) < IA2.getPuntuacion(instr,epsilon):
                mejorInstr = instr
        if IA2.getPuntuacion(mejorInstr, epsilon) > 0:
            for instr in IA2.hijos:
                if IA2.getPuntuacion(mejorInstr, epsilon) == IA2.getPuntuacion(instr, epsilon):
                    instrMejores.append(instr)
            instruccion2 = instrMejores[np.random.randint(0, len(instrMejores))]
        else:
            existe = True
            while existe:
                instruccion2 = generarInstruccionAleatoria(tableroPrueba2, 2)
                if code(instruccion2) not in IA2.hijos:
                    existe = False

    return instruccion1, instruccion2