from LN.Tablero import Tablero
import pygame

# Configuración pygame
TAMAÑO_CELDA = 78
TAMAÑO_BORDE = 4
TAMAÑO_LETRA = 16
TAMAÑO_ESTADO = TAMAÑO_LETRA*2+5
FONDO = (240, 230, 140)
LINEAS = (247-247//4, 217-217//4, 23-23//4)

FILAS = 5
COLUMNAS = 9

def iniciarPintador(tablero):
    pygame.init()  # Pygame inicializamos Pygame
    pygame.display.set_caption("Divasonian Crusaders 2: La venganza de los Romerianos")
    canvas = pygame.display.set_mode((COLUMNAS * TAMAÑO_CELDA + (COLUMNAS - 1) * TAMAÑO_BORDE, FILAS * TAMAÑO_CELDA + (FILAS - 1) * TAMAÑO_BORDE))
    canvas.fill(FONDO)
    font = pygame.font.SysFont("comicsansms", TAMAÑO_LETRA)  # Para el tipo de letra

    arqueroAzul = pygame.image.load("../Imagenes/ArqueroAzulC.png")
    barbaroAzul = pygame.image.load("../Imagenes/BarbaroAzulC.png")
    caballeroAzul = pygame.image.load("../Imagenes/CaballeroAzulC.png")
    guerreroAzul = pygame.image.load("../Imagenes/GuerreroAzulC.png")
    lanceroAzul = pygame.image.load("../Imagenes/LanceroAzulC.png")

    arqueroRojo = pygame.image.load("../Imagenes/ArqueroRojoC.png")
    barbaroRojo = pygame.image.load("../Imagenes/BarbaroRojoC.png")
    caballeroRojo = pygame.image.load("../Imagenes/CaballeroRojoC.png")
    guerreroRojo = pygame.image.load("../Imagenes/GuerreroRojoC.png")
    lanceroRojo = pygame.image.load("../Imagenes/LanceroRojoC.png")

    catapultaAzul = pygame.image.load("../Imagenes/CatapultaAzulC.png")
    coronaAzul = pygame.image.load("../Imagenes/CoronaAzul.png")

    catapultaRoja = pygame.image.load("../Imagenes/CatapultaRojaC.png")
    coronaRoja = pygame.image.load("../Imagenes/CoronaRojo.png")

    hacha = pygame.image.load("../Imagenes/HachaDivasonia.png")
    curarse = pygame.image.load("../Imagenes/CurarseC.png")
    colina = pygame.image.load("../Imagenes/ColinaC.png")
    proyectil = pygame.image.load("../Imagenes/impactoProyectilC.png")
    fondo = pygame.image.load("../Imagenes/capa.png")

    iconoRefachero = pygame.image.load("../Imagenes/iconoRefachero2.png")

    # arqueroAzul = pygame.image.load("./Imagenes/ArqueroAzulC.png")
    # barbaroAzul = pygame.image.load("./Imagenes/BarbaroAzulC.png")
    # caballeroAzul = pygame.image.load("./Imagenes/CaballeroAzulC.png")
    # guerreroAzul = pygame.image.load("./Imagenes/GuerreroAzulC.png")
    # lanceroAzul = pygame.image.load("./Imagenes/LanceroAzulC.png")
    #
    # arqueroRojo = pygame.image.load("./Imagenes/ArqueroRojoC.png")
    # barbaroRojo = pygame.image.load("./Imagenes/BarbaroRojoC.png")
    # caballeroRojo = pygame.image.load("./Imagenes/CaballeroRojoC.png")
    # guerreroRojo = pygame.image.load("./Imagenes/GuerreroRojoC.png")
    # lanceroRojo = pygame.image.load("./Imagenes/LanceroRojoC.png")
    #
    # catapultaAzul = pygame.image.load("./Imagenes/CatapultaAzulC.png")
    # coronaAzul = pygame.image.load("./Imagenes/CoronaAzul.png")
    #
    # catapultaRoja = pygame.image.load("./Imagenes/CatapultaRojaC.png")
    # coronaRoja = pygame.image.load("./Imagenes/CoronaRojo.png")
    #
    # hacha = pygame.image.load("./Imagenes/HachaDivasonia.png")
    # curarse = pygame.image.load("./Imagenes/CurarseC.png")
    # colina = pygame.image.load("./Imagenes/ColinaC.png")
    # fondo = pygame.image.load("./Imagenes/capa.png")
    #
    # iconoRefachero = pygame.image.load("./Imagenes/iconoRefachero2.png")

    arqueroAzul.convert()
    barbaroAzul.convert()
    caballeroAzul.convert()
    guerreroAzul.convert()
    lanceroAzul.convert()

    arqueroRojo.convert()
    barbaroRojo.convert()
    caballeroRojo.convert()
    guerreroRojo.convert()
    lanceroRojo.convert()

    catapultaAzul.convert()
    catapultaRoja.convert()

    coronaAzul.convert()
    coronaRoja.convert()

    hacha.convert()

    iconoRefachero.convert()
    pygame.display.set_icon(iconoRefachero) # Para ponerle un icono al programa

    i = 1
    while (i < COLUMNAS):
        pygame.draw.line(canvas, LINEAS, (i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1, 0), (
        i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1, FILAS * TAMAÑO_CELDA + (FILAS - 1) * TAMAÑO_BORDE - 1),
                         TAMAÑO_BORDE)
        i += 1
    i = 1
    while (i < FILAS):
        pygame.draw.line(canvas, LINEAS, (0, i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1), (
        COLUMNAS * TAMAÑO_CELDA + (COLUMNAS - 1) * TAMAÑO_BORDE - 1, i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1),
                         TAMAÑO_BORDE)
        i += 1
    turno = 0  # Reseteamos/iniciamos el contador de turno
    operacion = 0  # Reseteamos/iniciamos el contador de operacion

    pintar(canvas, tablero)

    return canvas

def pintar(canvas, tablero):

    pygame.event.get()

    arqueroAzul = pygame.image.load("../Imagenes/ArqueroAzulC.png")
    barbaroAzul = pygame.image.load("../Imagenes/BarbaroAzulC.png")
    caballeroAzul = pygame.image.load("../Imagenes/CaballeroAzulC.png")
    guerreroAzul = pygame.image.load("../Imagenes/GuerreroAzulC.png")
    lanceroAzul = pygame.image.load("../Imagenes/LanceroAzulC.png")

    arqueroRojo = pygame.image.load("../Imagenes/ArqueroRojoC.png")
    barbaroRojo = pygame.image.load("../Imagenes/BarbaroRojoC.png")
    caballeroRojo = pygame.image.load("../Imagenes/CaballeroRojoC.png")
    guerreroRojo = pygame.image.load("../Imagenes/GuerreroRojoC.png")
    lanceroRojo = pygame.image.load("../Imagenes/LanceroRojoC.png")

    catapultaAzul = pygame.image.load("../Imagenes/CatapultaAzulC.png")
    coronaAzul = pygame.image.load("../Imagenes/CoronaAzul.png")

    catapultaRoja = pygame.image.load("../Imagenes/CatapultaRojaC.png")
    coronaRoja = pygame.image.load("../Imagenes/CoronaRojo.png")

    hacha = pygame.image.load("../Imagenes/HachaDivasonia.png")
    curarse = pygame.image.load("../Imagenes/CurarseC.png")
    colina = pygame.image.load("../Imagenes/ColinaC.png")
    proyectil = pygame.image.load("../Imagenes/impactoProyectilC.png")
    fondo = pygame.image.load("../Imagenes/capa.png")

    iconoRefachero = pygame.image.load("../Imagenes/iconoRefachero2.png")

    # arqueroAzul = pygame.image.load("./Imagenes/ArqueroAzulC.png")
    # barbaroAzul = pygame.image.load("./Imagenes/BarbaroAzulC.png")
    # caballeroAzul = pygame.image.load("./Imagenes/CaballeroAzulC.png")
    # guerreroAzul = pygame.image.load("./Imagenes/GuerreroAzulC.png")
    # lanceroAzul = pygame.image.load("./Imagenes/LanceroAzulC.png")
    #
    # arqueroRojo = pygame.image.load("./Imagenes/ArqueroRojoC.png")
    # barbaroRojo = pygame.image.load("./Imagenes/BarbaroRojoC.png")
    # caballeroRojo = pygame.image.load("./Imagenes/CaballeroRojoC.png")
    # guerreroRojo = pygame.image.load("./Imagenes/GuerreroRojoC.png")
    # lanceroRojo = pygame.image.load("./Imagenes/LanceroRojoC.png")
    #
    # catapultaAzul = pygame.image.load("./Imagenes/CatapultaAzulC.png")
    # coronaAzul = pygame.image.load("./Imagenes/CoronaAzul.png")
    #
    # catapultaRoja = pygame.image.load("./Imagenes/CatapultaRojaC.png")
    # coronaRoja = pygame.image.load("./Imagenes/CoronaRojo.png")
    #
    # hacha = pygame.image.load("./Imagenes/HachaDivasonia.png")
    # curarse = pygame.image.load("./Imagenes/CurarseC.png")
    # colina = pygame.image.load("./Imagenes/ColinaC.png")
    # fondo = pygame.image.load("./Imagenes/capa.png")
    #
    # iconoRefachero = pygame.image.load("./Imagenes/iconoRefachero2.png")

    for pos, nodo in enumerate(tablero.nodos):
        x,y = pos%9, pos//9
        canvas.blit(fondo, (x*(TAMAÑO_CELDA+TAMAÑO_BORDE) , y*(TAMAÑO_CELDA+TAMAÑO_BORDE)))

        if type(nodo.casilla).__name__ == 'Colina':
            canvas.blit(colina, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.casilla).__name__ == 'Curacion':
            canvas.blit(curarse, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.casilla).__name__ == 'Catapulta' and nodo.casilla.identificador == 1:
            canvas.blit(catapultaAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.casilla).__name__ == 'Catapulta' and nodo.casilla.identificador == 2:
            canvas.blit(catapultaRoja, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.casilla).__name__ == 'Copa' and nodo.casilla.faccion == 1:
            canvas.blit(coronaAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.casilla).__name__ == 'Copa' and nodo.casilla.faccion == 2:
            canvas.blit(coronaRoja, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        if type(nodo.fichaDefensora).__name__ == 'Arquero' and nodo.fichaDefensora.faccion == 1:
            canvas.blit(arqueroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Arquero' and nodo.fichaDefensora.faccion == 2:
            canvas.blit(arqueroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Barbaro' and nodo.fichaDefensora.faccion == 1:
            canvas.blit(barbaroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Barbaro' and nodo.fichaDefensora.faccion == 2:
            canvas.blit(barbaroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Caballero' and nodo.fichaDefensora.faccion == 1:
            canvas.blit(caballeroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Caballero' and nodo.fichaDefensora.faccion == 2:
            canvas.blit(caballeroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Guerrero' and nodo.fichaDefensora.faccion == 1:
            canvas.blit(guerreroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Guerrero' and nodo.fichaDefensora.faccion == 2:
            canvas.blit(guerreroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Lancero' and nodo.fichaDefensora.faccion == 1:
            canvas.blit(lanceroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaDefensora).__name__ == 'Lancero' and nodo.fichaDefensora.faccion == 2:
            canvas.blit(lanceroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        if nodo.casilla.tieneHacha():
            canvas.blit(hacha, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        if type(nodo.fichaAtacante).__name__ == 'Arquero' and nodo.fichaAtacante.faccion == 1:
            canvas.blit(arqueroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Arquero' and nodo.fichaAtacante.faccion == 2:
            canvas.blit(arqueroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Barbaro' and nodo.fichaAtacante.faccion == 1:
            canvas.blit(barbaroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Barbaro' and nodo.fichaAtacante.faccion == 2:
            canvas.blit(barbaroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Caballero' and nodo.fichaAtacante.faccion == 1:
            canvas.blit(caballeroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Caballero' and nodo.fichaAtacante.faccion == 2:
            canvas.blit(caballeroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Guerrero' and nodo.fichaAtacante.faccion == 1:
            canvas.blit(guerreroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Guerrero' and nodo.fichaAtacante.faccion == 2:
            canvas.blit(guerreroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Lancero' and nodo.fichaAtacante.faccion == 1:
            canvas.blit(lanceroAzul, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))
        elif type(nodo.fichaAtacante).__name__ == 'Lancero' and nodo.fichaAtacante.faccion == 2:
            canvas.blit(lanceroRojo, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        if (nodo.fichaDefensora and nodo.fichaDefensora.tieneHacha()) or (nodo.fichaAtacante and nodo.fichaAtacante.tieneHacha()):
            canvas.blit(hacha, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        if nodo.cayoProyectil:
            canvas.blit(proyectil, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        pygame.display.update()

# tablero = Tablero()
# canvas = iniciarPintador(tablero)
# pintar(canvas, tablero)
# pygame.event.wait()
#
# import time
# time.sleep(5)
#
# print('Actualiza')
# pygame.event.get()
# pintar(canvas, tablero)
#
# import time
# time.sleep(5)
#
# print('Actualiza')
# pygame.event.wait()
# pintar(canvas, tablero)
#
# import time
# time.sleep(5)

# tablero = Tablero()
# tableroCopia = tablero.copy()
#
# print(tableroCopia)