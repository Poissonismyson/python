<<<<<<< HEAD
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
=======
#importare libreria copy

class Vertice:
    def __init__(self,x,y):
        #da completare a cura dello studente
        pass
    
class Triangolo:

    def __init__(self,a,b,c):
        #da completare a cura dello studente
        pass

    def copiaProfonda(self):
        #da completare a cura dello studente
        return None
    
    def copiaDebole(self):
        #da completare a cura dello studente
        return None

    def uguali(self,t):
        #da completare a cura dello studente
        return None
>>>>>>> 1a3d7b98b999b4e56004ea7967e618092a76fbf2
 