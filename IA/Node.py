from math import sqrt, log
import json

from MD.Fichas.Arquero import Arquero
from MD.Fichas.Guerrero import Guerrero
from MD.Instruccion.Operacion import *

def code(instruccion):
    if type(instruccion).__name__ == 'str':
        return instruccion
    else:
        string = ''
        for op in instruccion:
            if op is None:
                string += 'E,'
            else:
                string += op.code() + ','
        return string[:-1]

def decode(strinstruccion):
    instruccion = []
    splitted = strinstruccion.split(',')
    for op in splitted:
        if op == 'E':
            instruccion.append(None)
        else:
            instruccion.append(decodeOP(op))
    return instruccion

class Node:

    def __init__(self, wins, simulations, padre=None):
        self.hijos = {}
        self.wins = wins  # Puntos ganados o perdidos
        self.simulations = simulations
        self.padre = padre # Para el backpropagation

        self.ultimo = True

    def insert(self, instruccion, wins, simulations):
        self.hijos[code(instruccion)] = Node(wins, simulations, self)
        self.ultimo = False

    def get(self, instruccion):
        return self.hijos[instruccion]

    def getAll(self):
        return self.hijos

    def __str__(self, tabs=''):
        string = tabs + str(self.wins) + ' / ' + str(self.simulations)+'\n'
        for instruccion in self.hijos:
            string += instruccion + ' - ' + self.hijos[instruccion].__str__(tabs+'\t')
        return string

    def toJSON(self):
        jsonIni = '{' + '"wins":' + str(self.wins) + ',"simulations":' + str(self.simulations) + ',"hijos":' + '['
        jsonFin = ']' + '}'
        for instruccion in self.hijos:
            jsonIni += '{' + '"instruccion":"' + instruccion + '","hijo":' + self.hijos[instruccion].toJSON() + '}' + ','
        if len(self.hijos)>0:
            jsonIni = jsonIni[:-1]
        return jsonIni + jsonFin


    def puntuacion(self, instruccion, epsilon):
        if self.get(instruccion) == None:
            return 0
        else:
            return self.get(instruccion).wins/self.get(instruccion).simulations + epsilon*sqrt(log(self.simulations+1)/self.get(instruccion).simulations)

def fromJSON(jsonData):
    diccionario = json.loads(jsonData)
    return fromDictionary(diccionario)

def fromDictionary(diccionario):
    node = Node(int(diccionario['wins']),int(diccionario['simulations']))
    for hijo in diccionario['hijos']:
        nodeHijo = fromDictionary(hijo['hijo'])
        nodeHijo.padre = node
        node.hijos[hijo['instruccion']] = nodeHijo
    if len(diccionario['hijos'])>0:
        node.ultimo=False
    return node

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
# print(root.toJSON())
# print(json.loads(root.toJSON()))
# print(fromJSON(root.toJSON()))
