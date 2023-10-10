import numpy as np
from node import Node
from edge import Edges


class Graph:

    def __init__(self):
        '''
        Clase Grafo
        :atrib nodes: Diccionario los nodos del grafo
        :atrib edges: Lista de aristas del grafo
        '''
        self.nodes = {}
        self.edges = []

    def addNode(self, name):
        '''
        Agrega el nodo y sus atributos al diccionario
        :param name: nombre del nodo 
        '''
        node = self.nodes.get(name) 

        if node is None:
            self.nodes[name] = vars(Node())

   
    def addEdge(self, source, target, directed = False, auto = False):
        '''
        Agrega el nodo a la lista
        :param source: nodo origen
        :param target: nodo destino
        :param directed: dirigido
        :param auto: ciclos
        '''
        if auto is False:
            buc = source == target
        else:
            buc = False
        name = Edges(source, target)
        for edge in self.edges:
            if directed is False:
                comp = name != edge
            else:
                comp = False
            if name == edge or buc or comp:
                return False
        self.edges.append((name))

    def write(self, title, nodes):
        '''
        Genera archivo con formato GraphViz 
        :param title: titulo del archivo
        :param nodes: numero de nodos
        '''
        with open(f"{title}_{nodes}.gv", "w") as f:
            f.write('Graph = {\n')
            for node in self.nodes.keys():
                f.write(f'{node}\n')
            for edge in self.edges:
                edge = dir(edge)
                f.write(f'{edge[0]} -> {edge[1]}\n')
            f.write('}\n')
    
    def getDegree(self, node):
        '''
        Obtiene el número de aristas conectadas a un nodo 
        param: node: nodo
        :return grado del nodo
        '''
        deg = 0
        if len(self.edges) > 0:
            for nodes in self.edges:
                if dir(nodes)[0] == node or dir(nodes)[1] == node:
                    deg += 1
        return deg
         



