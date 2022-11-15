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

def Local_2J(nombre1, nombre2):
    rendicion1, rendicion2 = False, False
    partida = Partida()
    pintador = iniciarPintador(partida.tableroActual)

    print('Tablero del turno', partida.turno)
    print(partida.tableroActual)
    pintar(pintador, partida.tableroActual)

    while not partida.haTerminado:
        print('Comando del jugador 1:')
        time.sleep(0.001)
        comando1 = input()
        time.sleep(0.001)
        print('Comando del jugador 2:')
        time.sleep(0.001)
        comando2 = input()
        time.sleep(0.001)

        rendicion1 = comando1 == 'SURR'
        rendicion2 = comando2 == 'SURR'

        if rendicion1 or rendicion2:
            if rendicion1:
                print("El jugador", nombre1, "se ha rendido. Enhorabuena,", nombre2)
            if rendicion2:
                print("El jugador", nombre1, "se ha rendido. Enhorabuena,", nombre1)
            break

        instruccion1, instruccion2 = procesarComandos(comando1, comando2)

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

    while (True):  # Esperar para cerrar la pantalla
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit(0)  # salir del programa


def procesarComandos(comando1, comando2):

    comando1Splitted = comando1.replace(' ','').split(';')
    comando2Splitted = comando2.replace(' ','').split(';')

    f1, f2, o1, o2 = None, None, None, None
    instruccion1, instruccion2 = [], []

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

    for opComando in comando2Splitted:
        opElementos = opComando.split(',')
        o2 = None

        if opElementos[0] == 'mover':
            if opElementos[1]=='lancero': f2 = Lancero(2)
            elif opElementos[1]=='guerrero': f2 = Guerrero(2)
            elif opElementos[1]=='arquero': f2 = Arquero(2)
            elif opElementos[1]=='barbaro': f2 = Barbaro(2)
            elif opElementos[1]=='caballero': f2 = Caballero(2)

            if opElementos[2]=='N': o2 = Movimiento(f2,0)
            elif opElementos[2]=='NE': o2 = Movimiento(f2,1)
            elif opElementos[2]=='E': o2 = Movimiento(f2,2)
            elif opElementos[2]=='SE': o2 = Movimiento(f2,3)
            elif opElementos[2]=='S': o2 = Movimiento(f2,4)
            elif opElementos[2]=='SW': o2 = Movimiento(f2,5)
            elif opElementos[2]=='W': o2 = Movimiento(f2,6)
            elif opElementos[2]=='NW': o2 = Movimiento(f2,7)

        elif opElementos[0] == 'disparar':
            if opElementos[1]=='lancero': f2 = Lancero(2)
            elif opElementos[1]=='guerrero': f2 = Guerrero(2)
            elif opElementos[1]=='arquero': f2 = Arquero(2)
            elif opElementos[1]=='barbaro': f2 = Barbaro(2)
            elif opElementos[1]=='caballero': f2 = Caballero(2)

            # o2 = Disparo(f2, int(opElementos[2]))
            o2 = Disparo(f2, x=int(opElementos[2]), y=int(opElementos[3]))

        instruccion2.append(o2)

    return instruccion1, instruccion2

Local_2J('Jugador 1', 'Jugador 2')