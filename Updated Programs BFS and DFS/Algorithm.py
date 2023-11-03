from Graph import Graph
import random as rd
import math as mt
import numpy as np
import random as rd
import copy as cp
from edge import Edges



def Malla(n,m, directed = False):
    """
  Genera grafo de malla
  :param m: número de columnas (> 1)
  :param n: número de filas (> 1)
  :param dirigido: el grafo es dirigido?
  :Escribe el grafo
  """
    G = Graph()
    k = 0
    malla = []
    for i in range(m):
        fila = []
        for j in range(n):
            fila.append(k)
            G.addNode(k)
            k += 1
        malla.append(fila)
    
    for i in range(m):
        for j in range(n):
            if i<m-1:
                G.addEdge(malla[i][j], malla[i+1][j], directed)
            if j<n-1:
                G.addEdge(malla[i][j], malla[i][j+1], directed)

    G.write('Malla', G, n*m)
    return G
    

def ErdosRengy(n,m, directed = False, auto = False):
    """
  Genera grafo aleatorio con el modelo Erdos-Renyi
  :param n: número de nodos (> 0)
  :param m: número de aristas (>= n-1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G = Graph()
    for i in range(n):
        G.addNode(i)

    i=0
    while i < m:
        edge = G.addEdge(rd.randint(0,n-1), rd.randint(0,n-1), directed, auto)
        if edge is False:
            i = i
        else:
            i += 1
    G.write('ErgosRengy', G, n)
    return G

def Gilbert(n, p , directed = False, auto = False):
    """
  Genera grafo aleatorio con el modelo Gilbert
  :param n: número de nodos (> 0)
  :param p: probabilidad de crear una arista (0, 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G = Graph()
    for i in range(n):
        G.addNode(i)

    for i in range(n):
        for j in range(n):
            if rd.random() < p:
                if i != j:
                    G.addEdge(i, j)

    G.write('Gilbert', G, n)
    return G

def Geo(n, r ,directed = False, auto = False):

    G = Graph()
    for i in range(n):
        G.addNode(i)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                d = mt.dist(G.nodes.get(i).get('pos'),G.nodes.get(j).get('pos'))
                if d <= r:
                    G.addEdge(i,j, directed, auto)
    G.write('Geo', G, n)
    return G

def Barabási(n, d, directed = False, auto = False ):
    """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (> 0)
  :param d: grado máximo esperado por cada nodo (> 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G = Graph()
    G.addNode(0)

    for u in range(1, n):
        randomNodes = randomArray(u)
        G.addNode(u)
        for v in range(u):
            deg = G.getDegree(randomNodes[v])
            p = 1 - deg / d
            if rd.random() < p:
                if randomNodes[v] != u:
                    G.addEdge(u, randomNodes[v], directed, auto)
    G.write('Barabasi', G, n)
    return G

def DorogovtsevMendes(n, directed = False):
    """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (≥ 3)
  :param dirigido: el grafo es dirigido?
  :Escribe el grafo
  """
    G = Graph()
    for i in range(n):
        G.addNode(i)

    G.addEdge(0, 1, directed)
    G.addEdge(1, 2, directed)
    G.addEdge(0, 2, directed)
    for i in range(3, n):
        a = list(np.random.choice(G.edges))
        G.addEdge(a[0], i, directed)
        G.addEdge(a[1], i, directed)
    G.write('Dorogovtsev', G, n)
    return G
    
def randomArray(u):
    '''
    Crea un arreglo aletorio de nodos de 0 a u+1
    param u: numero de nodos
    return arreglo aletorio de nodos
    '''
    newarray = np.random.choice(u, u, replace=False)
    return newarray

def BFS(G,tnodes, mode, s = None):
    bfs = Graph()
    layers = []
    added = {}

    print('BFS started ...')
    if s is None:
        seed = rd.choice(list(G.nodes.keys()))
    else:
        seed = s
    n = bfs.addNode(seed)

    layers.append({seed: seed})
    added[seed] = seed
    
    i = 0
    while i < len(layers):
        nextlayer = {}
        curLayer = layers[i]

        for n in curLayer.values():
            edges = G.nodes[n]['edges']
            for e in edges:
                if e[0] == n:
                    m = e[1]
                else:
                    m = e[0]
                if m not in nextlayer and m not in added:
                    nn = bfs.addNode(n)
                    mm = bfs.addNode(m)

                    bfs.addEdge(n, m)
                    nextlayer[m] = m
                    added[m] = m                          
        i += 1
        if len(nextlayer) != 0:
            layers.append(nextlayer)
                                                 
    print('BFS finished ...')
    bfs.write(f'BFS_{mode}', bfs, tnodes)
    return bfs

def DFS(G, tnodes, mode, s=None):

    dfs = Graph()
    CopyG = cp.copy(G)
    added = []

    print('DFS started ...')
    if s is None:
        seed = rd.choice(list(CopyG.nodes.keys()))

    else:
        seed = s
    
    nodes = (CopyG.nodes)

    DFS_I(seed, dfs, added, nodes, tnodes, mode)
    DFS_R(seed, dfs, added, nodes, tnodes, mode)

def DFS_I(seed, dfs, added, nodes, tnodes, mode):
    dfs.addNode(seed)
    added.append(seed)

    CurNode = seed
    while len(dfs.nodes) < tnodes:
        

        if len(nodes[CurNode]['edges']) > 0:
    
            edge = rd.choice(nodes[CurNode]['edges'])
            nextNode = edge[1]

            if nextNode not in added:
                
                dfs.addNode(nextNode)
                dfs.addEdge(CurNode, nextNode)
                added.append(nextNode)

                nodes[CurNode]['edges'].remove(edge)
                invedge = [edge[1], edge[0]]
                nodes[nextNode]['edges'].remove(invedge)

                CurNode = nextNode
            else: 
                nodes[CurNode]['edges'].remove(edge)
                invedge = [edge[1], edge[0]]
                nodes[nextNode]['edges'].remove(invedge)
                CurNode = CurNode
        else:
            for e in dfs.edges:
                if list(e)[1] == CurNode:
                    CurNode = list(e)[0]

    print('DFS_I finished ...')
    dfs.write(f'DFS_I_{mode}', dfs, tnodes)        
    return dfs

def DFS_R(seed, dfs, added, nodes, tnodes, mode):
    dfs.addNode(seed)
    added.append(seed)


    for e in nodes[seed]['edges']:
        nextNode = e[1]
    
        if nextNode not in added:
            dfs.addNode(nextNode)
            dfs.addEdge(e)
            DFS_R(nextNode, dfs, added, nodes)
    print('DFS_R finished ...')
    dfs.write(f'DFS_R_{mode}', dfs, tnodes)        
    return dfs






