from copy import *
class Punto:
    pass

P1 = Punto()

P1.x = 3
P1.y = 4


DistanzaAlQuadrato = P1.x * P1.x + P1.y * P1.y

def StampaPunto(P):
    print( '(' + str(P.x) + ',' + str(P.y) + ')' )

def StessoPunto(P1, P2):
    return (P1.x == P2.x) and (P1.y == P2.y)

class Rettangolo:
    pass

Rett = Rettangolo()
Rett.Larghezza = 100
Rett.Altezza = 200

Rett.BassoSinistra = Punto()
Rett.BassoSinistra.x = 0
Rett.BassoSinistra.y = 0

def TrovaCentro(Rettangolo):
    P = Punto()
    P.x = Rettangolo.BassoSinistra.x + Rettangolo.Larghezza/2
    P.y = Rettangolo.BassoSinistra.y + Rettangolo.Altezza/2
    return P

Rett.Larghezza = Rett.Larghezza + 50
Rett.Altezza = Rett.Altezza + 100

def AumentaRettangolo(Rett, AumentoLargh,AumentoAlt):
    NuovoRett = deepcopy(Rett)
    NuovoRett.Larghezza = NuovoRett.Larghezza + AumentoLargh
    NuovoRett.Altezza = NuovoRett.Altezza + AumentoAlt
    return NuovoRett

R1 = Rettangolo()
R1.Larghezza = 100
R1.Altezza = 200
R1.BassoSinistra = Punto()
R1.BassoSinistra.x = 0
R1.BassoSinistra.y = 0
AumentaRettangolo(R1, 50, 100)

Centro = TrovaCentro(Rett)
StampaPunto(Centro)

Centro = TrovaCentro(R1)
StampaPunto(Centro)

R2 = AumentaRettangolo(R1, 50, 100)
AumentaRettangolo(R1, 50, 100)



R1.BassoSinistra.x = 1
print(R2.BassoSinistra.x)  
R2.BassoSinistra.x = 2
print(R2.BassoSinistra.x) 

Centro = TrovaCentro(R2)
StampaPunto(Centro)

Centro = TrovaCentro(R1)
StampaPunto(Centro)

from copy import copy

P1 = Punto ()
P1.x = 3
P1.y = 4

P2 = copy(P1)

print(P1 == P2)

print(StessoPunto(P1, P2))


R2.BassoSinistra.x =  1
print(R1.BassoSinistra.x)

print(R2 is R1)

R2 == R1

from copy import deepcopy

