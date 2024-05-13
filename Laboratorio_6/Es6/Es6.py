<<<<<<< HEAD
from math import tan, pi

class Poligono:
    def __init__(self, l, n):
        self.lunghezza = l
        self.nlati = n


    def perimetro(self):
        self.p = self.lunghezza * self.nlati
        return self.p

    def stampaPerimetro(self):
        print(self.perimetro())

    def apotema(self):
        self.apo = (self.lunghezza)/(2*tan(pi/self.nlati))
        return self.apo

    def stampaApotema(self):
        print(self.apotema())

    def area(self):
        self.ar = (self.perimetro() * self.apotema())/ 2
        return self.ar

    def stampaArea(self):
        print(self.area())
=======
#importare libreria math

class Poligono:
    def __init__(self, l, n):
        #da completare a cura dello studente
        pass 

    def perimetro(self):
        #da completare a cura dello studente
        return None

    def stampaPerimetro(self):
        #da completare a cura dello studente
        pass

    def apotema(self):
        #da completare a cura dello studente
        return None

    def stampaApotema(self):
        #da completare a cura dello studente
        pass

    def area(self):
        #da completare a cura dello studente
        return None

    def stampaArea(self):
        #da completare a cura dello studente
        pass
>>>>>>> 1a3d7b98b999b4e56004ea7967e618092a76fbf2
