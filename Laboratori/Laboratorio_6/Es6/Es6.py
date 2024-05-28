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
