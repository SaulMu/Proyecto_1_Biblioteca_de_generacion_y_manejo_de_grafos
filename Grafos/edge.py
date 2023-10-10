
class Edges:
    'Clase Nodo'
    def __init__(self, source, target):
        '''
        :atrib source: origen de arista
        :atrib target: destino de arista
        '''
        self.n0 = source
        self.n1 = target

    def __dir__(self):
        'Rregresa la rita como una lista 1x2'
        return [self.n0, self.n1]

    def __eq__(self, other):
        'Compara que dos aristas sean iguales'
        if isinstance(other, Edges):
            return (self.n0 == other.n0 and self.n1 == other.n1) 
        return False
    
    def __ne__(self, other):
        'Compara aristas para evitar un digrafo'
        if isinstance(other, Edges):
            return (self.n0 == other.n1 and self.n1 == other.n0) 
        return False 


