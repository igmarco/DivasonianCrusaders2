from LN.Tablero import Tablero
from Utilidades.Utilidades import Direccion


class Partida():

    def __init__(self, tableroActual=None, turno=0, haTerminado=False):
        self.tableroActual = tableroActual if tableroActual is not None else Tablero()
        self.tablerosMovimientos = []

        self.turno=turno
        self.haTerminado=haTerminado

    def ejecutarTurno(self, instruccion1, instruccion2):
        self.tablerosMovimientos.clear()
        for movimiento in range(6):
            self.ejecutarOperacion(instruccion1[movimiento], instruccion2[movimiento])
            self.tablerosMovimientos.append(self.tableroActual.copy())
            self.tableroActual.limpiarProyectiles()
        self.turno=self.turno+1
        self.tableroActual.resolverTurno()
        self.haTerminado = self.tableroActual.haTerminado()

    def ejecutarOperacion(self, op1, op2):
        if type(op1).__name__ == 'Movimiento' and not self.tableroActual.movimientoPosible(op1.ficha):
            op1 = None
        if type(op2).__name__ == 'Movimiento' and not self.tableroActual.movimientoPosible(op2.ficha):
            op2 = None

        if op1 is None:
            if op2 is not None:
                if type(op2).__name__ == 'Movimiento':
                    self.tableroActual.moverFichaDireccion(op2.ficha, op2.direccion)
                elif type(op2).__name__ == 'Disparo':
                    self.tableroActual.dispararProyectiles(self.tableroActual.nodos[self.tableroActual.dondeEsta(op2.ficha)].casilla, op2.x, op2.y, op2.ficha)
        elif op2 is None:
            if type(op1).__name__ == 'Movimiento':
                self.tableroActual.moverFichaDireccion(op1.ficha, op1.direccion)
            elif type(op1).__name__ == 'Disparo':
                self.tableroActual.dispararProyectiles(self.tableroActual.nodos[self.tableroActual.dondeEsta(op1.ficha)].casilla, op1.x, op1.y, op1.ficha)

        else:
            if type(op2).__name__ == 'Disparo':
                if type(op1).__name__ == 'Movimiento':
                    self.tableroActual.moverFichaDireccion(op1.ficha, op1.direccion)
                elif type(op1).__name__ == 'Disparo':
                    self.tableroActual.dispararProyectiles(self.tableroActual.nodos[self.tableroActual.dondeEsta(op1.ficha)].casilla, op1.x, op1.y, op1.ficha)
                self.tableroActual.dispararProyectiles(self.tableroActual.nodos[self.tableroActual.dondeEsta(op2.ficha)].casilla, op2.x, op2.y, op2.ficha)
            elif type(op1).__name__ == 'Disparo':
                if type(op2).__name__ == 'Movimiento':
                    self.tableroActual.moverFichaDireccion(op2.ficha, op2.direccion)
                elif type(op2).__name__ == 'Disparo':
                    self.tableroActual.dispararProyectiles(self.tableroActual.nodos[self.tableroActual.dondeEsta(op2.ficha)].casilla, op2.x, op2.y, op2.ficha)
                self.tableroActual.dispararProyectiles(self.tableroActual.nodos[self.tableroActual.dondeEsta(op1.ficha)].casilla, op1.x, op1.y, op1.ficha)

            else:
                self.tableroActual.moverFichasALaVez(op1.ficha,op1.direccion, op2.ficha, op2.direccion)

