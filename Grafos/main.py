from Algorithm import ErdosRengy, Malla, Gilbert, Geo, Barabási, DorogovtsevMendes

def pedir():
    op = int(input(
        '''◈════Escoja el algoritmo════◈:
        1)Modelo Gm,n de malla
        2)Modelo Gn,m de Erdös y Rényi
        3)Modelo Gn,p de Gilbert
        4)Modelo Gn,r geográfico simple
        5)Variante del modelo Gn,d Barabási-Albert
        6)Modelo Gn Dorogovtsev-Mendes
        ≫'''))
    
    switch(op)

def switch(op):
    'Pide los parametro y manda a llamar a los algoritmos'
    if op == 1:
        while True:
            n = int(input('Numero de columnas: '))
            if n > 1:
                break
        while True:    
            m = int(input('Numero de filas: '))
            if m > 1:
                break
        d = directed()
        Malla(n, m, d)
    elif op == 2:
        while True:
            n = int(input('Numero de nodos: '))
            if n>0:
                break
        while True:
            m = int(input('Numero de aristas: '))
            if m >= n - 1:
                break
        d = directed()
        a = auto()
        ErdosRengy(n, m, d, a)
    elif op == 3:
        while True:
            n = int(input('Numero de nodos: '))
            if n > 0:
                break
        while True:
            p = float(input('Probabilidad: '))
            if p > 0 and p < 1:
                break
        d = directed()
        a = auto()
        Gilbert(n, p, d, a)
    elif op == 4:
        while True:
            n = int(input('Numero de nodos: '))
            if n > 0:
                break
        while True:
            r = float(input('Distancia: '))
            if r > 0 and r < 1:
                break
        d = directed()
        a = auto()
        Geo(n, r, d, a)       
    elif op == 5:
        while True:
            n = int(input('Numero de nodos: '))
            if n > 0:
                break
        while True:
            d = float(input('Grado maximo: '))
            if d > 1:
                break
        di = directed()
        a = auto()
        Barabási(n, d, di, a)   
    elif op == 6:
        while True:
            n = int(input('Numero de nodos: '))
            if n >= 3:
                break
        d = directed()
        DorogovtsevMendes(n, d)   
    else:
        pedir()

def directed():
    'Define si el grafo es dirigido'
    d = input('¿Dirigido? Y/N = ')
    if d == 'N':
        return False
    elif d == 'Y':
        return True
    else:
        directed()

def auto():
    'Define si el grafo contiene bucles'
    a = input('¿Bluces? Y/N = ')
    if a == 'N':
        return False
    elif a == 'Y':
        return True
    else:
        auto()

pedir()