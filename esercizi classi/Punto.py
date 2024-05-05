
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    def __add__(self, Punto2): 
        return Punto(self.x + Punto2.x, self.y + Punto2.y)
    def __sub__(self, Punto2): 
        return Punto(self.x - Punto2.x, self.y - Punto2.y) 
    def __mul__(self, Punto2):  
        return Punto(self.x * Punto2.x, self.y * Punto2.y)
    def __truediv__(self, Punto2):
        return Punto(self.x / Punto2.x, self.y / Punto2.y)
    def __eq__(self, Punto2):
        return (self.x == Punto2.x) and (self.y == Punto2.y)
P = Punto(3, 4)
print(P)

P1 = Punto(3, 4)
P2 = Punto(5, 7)
P3 = P1 + P2
print(P3)