from LN.Tablero import Tablero

class Partida():

    def __init__(self, tableroActual=None, turno=0, haTerminado=False):
        self.tableroActual = tableroActual if tableroActual is not None else Tablero()
        self.tablerosMovimientos = []

        self.turno=turno
        self.haTerminado=haTerminado

    def ejecutarTurno(self, instruccion1, instruccion2):
        self.tablerosMovimientos.clear()
        tableroAnterior = self.tableroActual
        for movimiento in range(6):
            self.ejecutarOperacion(instruccion1[movimiento], instruccion2[movimiento])
            self.tablerosMovimientos.append(self.tableroActual.copy()) # Importante!! Implementar .copy()
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
                    self.tableroActual.moverFicha(op2.ficha, op2.direccion)
                elif type(op2).__name__ == 'Disparo':
                    self.tableroActual.dispararProyectiles(op2.catapulta, op2.x, op2.y, op2.ficha)
        elif op2 is None:
            if type(op1).__name__ == 'Movimiento':
                self.tableroActual.moverFicha(op1.ficha, op1.direccion)
            elif type(op1).__name__ == 'Disparo':
                self.tableroActual.dispararProyectiles(op1.catapulta, op1.x, op1.y, op1.ficha)

        else:
            if type(op2).__name__ == 'Disparo':
                if type(op1).__name__ == 'Movimiento':
                    self.tableroActual.moverFicha(op1.ficha, op1.direccion)
                elif type(op1).__name__ == 'Disparo':
                    self.tableroActual.dispararProyectiles(op1.catapulta, op1.x, op1.y, op1.ficha)
                self.tableroActual.dispararProyectiles(op2.catapulta, op2.x, op2.y, op2.ficha)
            elif type(op1).__name__ == 'Disparo':
                if type(op2).__name__ == 'Movimiento':
                    self.tableroActual.moverFicha(op2.ficha, op2.direccion)
                elif type(op2).__name__ == 'Disparo':
                    self.tableroActual.dispararProyectiles(op2.catapulta, op2.x, op2.y, op2.ficha)
                self.tableroActual.dispararProyectiles(op1.catapulta, op1.x, op1.y, op1.ficha)

            else:
                self.tableroActual.moverFichasALaVez(op1.ficha,op1.direccion, op2.ficha, op2.direccion)

