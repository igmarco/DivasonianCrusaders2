import sys
from datetime import datetime
from treelib import Node, Tree

from LN.Partida import Partida
from MD.Fichas.Arquero import Arquero
from MD.Fichas.Barbaro import Barbaro
from MD.Fichas.Caballero import Caballero
from MD.Fichas.Guerrero import Guerrero
from MD.Fichas.Lancero import Lancero
from MD.Instruccion.Operacion import Movimiento, Disparo
from Presentacion.Pintador import *

def crearIA():
    pass

def cargarIA(nombre):
    pass

def guardarIA(nombre, IA):
    f = open('IA_'+nombre+'_'+datetime.now().date()+'.txt', 'w')
    f.write(IA.to_json(with_data=True))
    f.close()

ia = Tree()
ia.create_node([1,35],'e,e,mcE,e,e,e')
subia = Tree()
subia.create_node([1,37],'CW,e,e,e,BW,LSW')
ia.paste(subia.root,subia)
ia.show()

# def entrenarIAs(IA1, IA2):
#     rendicion1, rendicion2 = False, False
#     turno = 0
#     partida = Partida()
#     pintador = iniciarPintador(partida.tableroActual)
#
#     print('Tablero del turno', partida.turno)
#     print(partida.tableroActual)
#     pintar(pintador, partida.tableroActual)
#
#     while not partida.haTerminado:
#         print('Comando del jugador 1:')
#         time.sleep(0.001)
#         comando1 = input()
#         time.sleep(0.001)
#         print('Comando del jugador 2:')
#         time.sleep(0.001)
#         comando2 = input()
#         time.sleep(0.001)
#
#         rendicion1 = comando1 == 'SURR'
#         rendicion2 = comando2 == 'SURR'
#
#         if rendicion1 or rendicion2:
#             if rendicion1:
#                 print("El jugador", nombre1, "se ha rendido. Enhorabuena,", nombre2)
#             if rendicion2:
#                 print("El jugador", nombre1, "se ha rendido. Enhorabuena,", nombre1)
#             break
#
#         instruccion1, instruccion2 = procesarComandos(partida, comando1, comando2)
#
#         partida.ejecutarTurno(instruccion1, instruccion2)
#
#         # for ind, tablero in enumerate(partida.tablerosMovimientos):
#         #     print('Tablero',ind, 'del turno', partida.turno)
#         #     print(tablero)
#         #
#         #     time.sleep(2)
#         #     pintar(pintador, tablero)
#
#         print('Tablero final del turno', partida.turno)
#         print(partida.tableroActual)
#         pintar(pintador, partida.tableroActual)
#
#     if partida.tableroActual.getGanador() == 1:
#         print('Enhorabuena, ha ganado', nombre1, 'en el turno', partida.turno)
#     if partida.tableroActual.getGanador() == 2:
#         print('Enhorabuena, ha ganado', nombre1, 'en el turno', partida.turno)
#     elif partida.tableroActual.getGanador() == 0:
#         print('Nada mal,', nombre1, 'y', nombre2, ', ha habido un empate en el turno', partida.turno)
#
#     while (True):  # Esperar para cerrar la pantalla
#         pygame.event.pump()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.display.quit()
#                 pygame.quit()
#                 sys.exit(0)  # salir del programa