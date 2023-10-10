from Graph import Graph
import random as rd
import math as mt
import numpy as np
import random as rd

G = Graph()

def Malla(n,m, directed = False):
    """
  Genera grafo de malla
  :param m: número de columnas (> 1)
  :param n: número de filas (> 1)
  :param dirigido: el grafo es dirigido?
  :Escribe el grafo
  """
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

    G.write('Malla', n*m)
    

def ErdosRengy(n,m, directed = False, auto = False):
    """
  Genera grafo aleatorio con el modelo Erdos-Renyi
  :param n: número de nodos (> 0)
  :param m: número de aristas (>= n-1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    for i in range(n):
        G.addNode(i)

    i=0
    while i < m:
        edge = G.addEdge(rd.randint(0,n-1), rd.randint(0,n-1), directed, auto)
        if edge is False:
            i = i
        else:
            i += 1
    G.write('ErgosRengy', n)

def Gilbert(n, p , directed = False, auto = False):
    """
  Genera grafo aleatorio con el modelo Gilbert
  :param n: número de nodos (> 0)
  :param p: probabilidad de crear una arista (0, 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    for i in range(n):
        G.addNode(i)

    for i in range(n):
        for j in range(n):
            if rd.random() < p:
                if i != j:
                    G.addEdge(i, j)

    G.write('Gilbert', n)

def Geo(n, r ,directed = False, auto = False):
    for i in range(n):
        G.addNode(i)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                d = mt.dist(G.nodes.get(i).get('pos'),G.nodes.get(j).get('pos'))
                if d <= r:
                    G.addEdge(i,j, directed, auto)
    G.write('Geo', n)

def Barabási(n, d, directed = False, auto = False ):
    """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (> 0)
  :param d: grado máximo esperado por cada nodo (> 1)
  :param dirigido: el grafo es dirigido?
  :param auto: permitir auto-ciclos?
  :Escribe el grafo
  """
    G.addNode(0)

    for u in range(1, n):
        randomNodes = randomArray(u)
        for v in range(u):
            deg = G.getDegree(randomNodes[v])
            p = 1 - deg / d
            if rd.random() < p:
                if randomNodes[v] != u:
                    G.addEdge(u, randomNodes[v], directed, auto)
        G.addNode(u)
    G.write('Barabasi', n)

def DorogovtsevMendes(n, directed = False):
    """
  Genera grafo aleatorio con el modelo Barabasi-Albert
  :param n: número de nodos (≥ 3)
  :param dirigido: el grafo es dirigido?
  :Escribe el grafo
  """
    for i in range(n):
        G.addNode(i)

    G.addEdge(0, 1, directed)
    G.addEdge(1, 2, directed)
    G.addEdge(0, 2, directed)
    for i in range(3, n):
        a = dir(np.random.choice(G.edges))
        G.addEdge(a[0], i, directed)
        G.addEdge(a[1], i, directed)
    G.write('Dorogovtsev', n)
    
def randomArray(u):
    '''
    Crea un arreglo aletorio de nodos de 0 a u+1
    param u: numero de nodos
    return arreglo aletorio de nodos
    '''
    newarray = np.random.choice(u, u, replace=False)
    return newarray

