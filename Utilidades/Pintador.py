from LN import Tablero
import pygame

# Configuración pygame
TAMAÑO_CELDA = 64
TAMAÑO_BORDE = 4
TAMAÑO_LETRA = 16
TAMAÑO_ESTADO = TAMAÑO_LETRA*2+5
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

STEP_PAUSE = 0.3
LRN_PAUSE = 0.001
EPISODE_PAUSE = 0.1

FILAS = 9
COLUMNAS = 2

def iniciar(tablero):
    pygame.init()  # Pygame inicializamos Pygame
    pygame.display.set_caption("Divasonian Crusaders 2: La venganza de los Romerianos")
    canvas = pygame.display.set_mode((FILAS * TAMAÑO_CELDA + (FILAS - 1) * TAMAÑO_BORDE, COLUMNAS * TAMAÑO_CELDA + (COLUMNAS - 1) * TAMAÑO_BORDE))
    canvas.fill(WHITE)
    font = pygame.font.SysFont("comicsansms", TAMAÑO_LETRA)  # Para el tipo de letra

    arqueroAzul = pygame.image.load("Imagenes/ArqueroAzulC.png")
    barbaroAzul = pygame.image.load("Imagenes/BarbaroAzulC.png")
    caballeroAzul = pygame.image.load("Imagenes/CaballeroAzulC.png")
    guerreroAzul = pygame.image.load("Imagenes/GuerreroAzulC.png")
    lanceroAzul = pygame.image.load("Imagenes/LanceroAzulC.png")

    arqueroRojo = pygame.image.load("Imagenes/ArqueroRojoC.png")
    barbaroRojo = pygame.image.load("Imagenes/BarbaroRojoC.png")
    caballeroRojo = pygame.image.load("Imagenes/CaballeroRojoC.png")
    guerreroRojo = pygame.image.load("Imagenes/GuerreroRojoC.png")
    lanceroRojo = pygame.image.load("Imagenes/LanceroRojoC.png")

    catapultaAzul = pygame.image.load("Imagenes/CatapultaAzulC.png")
    coronaAzul = pygame.image.load("Imagenes/CoronaAzulC.png")

    catapultaRoja = pygame.image.load("Imagenes/CatapultaRojaC.png")
    coronaRoja = pygame.image.load("Imagenes/CoronaRojaC.png")

    hacha = pygame.image.load("Imagenes/HachaDivasonia.png")
    curarse = pygame.image.load("Imagenes/CurarseC.png")
    colina = pygame.image.load("Imagenes/ColinaC.png")
    fondo = pygame.image.load("Imagenes/fondo.png")

    iconoRefachero = pygame.image.load("Imagenes/iconoRefachero2.png")

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
        pygame.draw.line(canvas, BLACK, (i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1, 0), (
        i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1, FILAS * TAMAÑO_CELDA + (FILAS - 1) * TAMAÑO_BORDE - 1),
                         TAMAÑO_BORDE)
        i += 1
    i = 1
    while (i < FILAS):
        pygame.draw.line(canvas, BLACK, (0, i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1), (
        COLUMNAS * TAMAÑO_CELDA + (COLUMNAS - 1) * TAMAÑO_BORDE - 1, i * TAMAÑO_CELDA + (i - 1) * TAMAÑO_BORDE + 1),
                         TAMAÑO_BORDE)
        i += 1
    turno = 0  # Reseteamos/iniciamos el contador de turno
    operacion = 0  # Reseteamos/iniciamos el contador de operacion

    pintar(canvas, tablero)

    return canvas

def pintar(canvas, tablero):
    arqueroAzul = pygame.image.load("Imagenes/ArqueroAzulC.png")
    barbaroAzul = pygame.image.load("Imagenes/BarbaroAzulC.png")
    caballeroAzul = pygame.image.load("Imagenes/CaballeroAzulC.png")
    guerreroAzul = pygame.image.load("Imagenes/GuerreroAzulC.png")
    lanceroAzul = pygame.image.load("Imagenes/LanceroAzulC.png")

    arqueroRojo = pygame.image.load("Imagenes/ArqueroRojoC.png")
    barbaroRojo = pygame.image.load("Imagenes/BarbaroRojoC.png")
    caballeroRojo = pygame.image.load("Imagenes/CaballeroRojoC.png")
    guerreroRojo = pygame.image.load("Imagenes/GuerreroRojoC.png")
    lanceroRojo = pygame.image.load("Imagenes/LanceroRojoC.png")

    catapultaAzul = pygame.image.load("Imagenes/CatapultaAzulC.png")
    coronaAzul = pygame.image.load("Imagenes/CoronaAzulC.png")

    catapultaRoja = pygame.image.load("Imagenes/CatapultaRojaC.png")
    coronaRoja = pygame.image.load("Imagenes/CoronaRojaC.png")

    hacha = pygame.image.load("Imagenes/HachaDivasonia.png")
    curarse = pygame.image.load("Imagenes/CurarseC.png")
    colina = pygame.image.load("Imagenes/ColinaC.png")
    fondo = pygame.image.load("Imagenes/fondo.png")

    iconoRefachero = pygame.image.load("Imagenes/iconoRefachero2.png")

    for pos, nodo in tablero.nodos:
        x,y = pos%9+1, 4-pos//9+1
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

        if nodo.casilla.tieneHacha() or nodo.fichaDefensora.tieneHacha() or nodo.fichaAtacante.tieneHacha():
            canvas.blit(hacha, (x * (TAMAÑO_CELDA + TAMAÑO_BORDE), y * (TAMAÑO_CELDA + TAMAÑO_BORDE)))

        pygame.display.update()

tablero = Tablero()
canvas = iniciar(tablero)
pintar(canvas, tablero)
