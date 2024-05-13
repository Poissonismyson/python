import copy

class Vertice:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    
class Triangolo:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def copiaProfonda(self):
        deepcopia = copy.deepcopy(self)
        return deepcopia
    
    def copiaDebole(self):
        copia = copy.copy(self) 
        return copia

    def uguali(self,t):
        if self.a == t.a and self.b == t.b and self.c == t.c:
            return True
        else:
            return False
 