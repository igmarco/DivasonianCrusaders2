import sys
import os
import time
from datetime import datetime

import numpy as np
import math as m

from IA.Node import Node, fromJSON, code, decode
from LN.Partida import Partida
from MD.Casillas.Catapulta import Catapulta
from MD.Instruccion.Operacion import Movimiento, Disparo
from Presentacion.Pintador import *
from Utilidades.Utilidades import Direccion

import sys

epsilon = m.sqrt(2)

def cargarIA(nombre):
    sys.setrecursionlimit(1500)

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

def entrenarIAs(nombre1, nombre2, partidas=100, pintarTableros=False, sleep=0.1):

    print('Cargando...')
    IA1 = cargarIA(nombre1)
    IA2 = cargarIA(nombre2)
    print('Cargado')

    if IA1 is None or IA2 is None:
        print('Error al cargar las IAs')
    else:
        entrenar(IA1, IA2, nombre1, nombre2, partidas, pintarTableros, sleep)

def entrenar(IA1, IA2, nombre1, nombre2, partidas, pintarTableros=False, sleep=0.1):
    nodoraiz1 = IA1
    nodoraiz2 = IA2
    for i in range(partidas):
        partida = Partida()
        if pintarTableros:
            pintador = iniciarPintador(partida.tableroActual)

        IA1 = nodoraiz1
        IA2 = nodoraiz2

        print('Partida', i)

        # print('Tablero del turno', partida.turno)
        # print(partida.tableroActual)

        if pintarTableros:
            pintar(pintador, partida.tableroActual)

        turnosNoAleatorios = 0

        while not partida.haTerminado:
            instruccion1, instruccion2, aleatoria = elegirInstrucciones(IA1, IA2, partida)
            turnosNoAleatorios += 0 if aleatoria else 1

            if code(instruccion1) in IA1.hijos:
                IA1 = IA1.get(code(instruccion1))
            else:
                IA1.insert(instruccion1,0,0)
                IA1 = IA1.get(code(instruccion1))
            if code(instruccion2) in IA2.hijos:
                IA2 = IA2.get(code(instruccion2))
            else:
                IA2.insert(instruccion2,0,0)
                IA2 = IA2.get(code(instruccion2))

            codigoTablero = partida.tableroActual.codeTB()
            if codigoTablero in IA1.hijos:
                IA1 = IA1.get(codigoTablero)
            else:
                IA1.insert(codigoTablero, 0, 0)
                IA1 = IA1.get(code(codigoTablero))
            if code(codigoTablero) in IA2.hijos:
                IA2 = IA2.get(code(codigoTablero))
            else:
                IA2.insert(codigoTablero, 0, 0)
                IA2 = IA2.get(code(codigoTablero))


            # print(code(instruccion1))
            # print(code(instruccion2))
            partida.ejecutarTurno(instruccion1, instruccion2)

            if pintarTableros:
                for ind, tablero in enumerate(partida.tablerosMovimientos):
                    # print('Tablero',ind, 'del turno', partida.turno)
                    # print(tablero)
                    time.sleep(sleep)
                    pintar(pintador, tablero)

            # print('Tablero final del turno', partida.turno)
            # print(partida.tableroActual)

            if pintarTableros:
                pintar(pintador, partida.tableroActual)

        if partida.tableroActual.getGanador() == 1:
            print('Enhorabuena, ha ganado', nombre1, 'en el turno', partida.turno, ' (' + str(turnosNoAleatorios), 'turnos no aleatorios)')
        if partida.tableroActual.getGanador() == 2:
            print('Enhorabuena, ha ganado', nombre2, 'en el turno', partida.turno, ' (' + str(turnosNoAleatorios), 'turnos no aleatorios)')
        elif partida.tableroActual.getGanador() == 0:
            print('Nada mal,', nombre1, 'y', nombre2 + ', ha habido un empate en el turno', partida.turno, ' (' + str(turnosNoAleatorios), 'turnos no aleatorios)')

        #Aquí toca hacer el back propagation.
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

        nodoBP = IA2
        if partida.tableroActual.getGanador() == 2:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 1 + (0.25 - partida.turno*0.005)
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 1:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins - 1 + (0.25 - partida.turno*0.005)
                nodoBP = nodoBP.padre
        elif partida.tableroActual.getGanador() == 0:
            while nodoBP.padre is not None:
                nodoBP.simulations = nodoBP.simulations + 1
                nodoBP.wins = nodoBP.wins + 0 + (0.25 - partida.turno*0.005)
                nodoBP = nodoBP.padre

    print('Guardando...')
    guardarIA(nombre1, nodoraiz1)
    guardarIA(nombre2, nodoraiz2)
    print('Guardado')

    if pintarTableros:
        while (True):  # Esperar para cerrar la pantalla
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit(0)  # salir del programa

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

def elegirInstrucciones(IA1, IA2, partida):
    instruccion1, instruccion2 = [], []

    tableroPrueba1 = partida.tableroActual.copy()
    tableroPrueba2 = partida.tableroActual.copy()

    aleatoria = False

    if IA1.ultimo:
        instruccion1 = generarInstruccionAleatoria(tableroPrueba1, 1)
        aleatoria = True
    else:
        instrMejores = []
        mejorInstr = list(IA1.hijos.keys())[0]
        for instr in IA1.hijos:
            if IA1.puntuacion(mejorInstr,epsilon) < IA1.puntuacion(instr,epsilon):
                mejorInstr = instr
        if IA1.puntuacion(mejorInstr, epsilon) > 0:
            for instr in IA1.hijos:
                if IA1.puntuacion(mejorInstr, epsilon) == IA1.puntuacion(instr, epsilon):
                    instrMejores.append(instr)
            instruccion1 = decode(instrMejores[np.random.randint(len(instrMejores))])
        else:
            existe = True
            while existe:
                instruccion1 = generarInstruccionAleatoria(tableroPrueba1, 1)
                aleatoria = True
                if code(instruccion1) not in IA1.hijos:
                    existe = False

    if IA2.ultimo:
        instruccion2 = generarInstruccionAleatoria(tableroPrueba2, 2)
    else:
        instrMejores = []
        mejorInstr = list(IA2.hijos.keys())[0]
        for instr in IA2.hijos:
            if IA2.puntuacion(mejorInstr,epsilon) < IA2.puntuacion(instr,epsilon):
                mejorInstr = instr
        if IA2.puntuacion(mejorInstr, epsilon) > 0:
            for instr in IA2.hijos:
                if IA2.puntuacion(mejorInstr, epsilon) == IA2.puntuacion(instr, epsilon):
                    instrMejores.append(instr)
            instruccion2 = decode(instrMejores[np.random.randint(0, len(instrMejores))])
        else:
            existe = True
            while existe:
                instruccion2 = generarInstruccionAleatoria(tableroPrueba2, 2)
                if code(instruccion2) not in IA2.hijos:
                    existe = False

    return instruccion1, instruccion2, aleatoria

# IA1 = Node(0,0)
# IA2 = Node(0,0)
# guardarIA('Divasonianos', IA1)
# guardarIA('Romerianos', IA2)

entrenarIAs('Divasonianos', 'Romerianos', 10000, pintarTableros=False)
# entrenarIAs('Divasonianos', 'Romerianos', 25, pintarTableros=True)
# entrenarIAs('Divasonianos', 'Romerianos', 1, pintarTableros=True, sleep=0.1)