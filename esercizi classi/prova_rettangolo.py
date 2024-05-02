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

Centro = TrovaCentro(Rett)
StampaPunto(Centro)

Rett.Larghezza = Rett.Larghezza + 50
Rett.Altezza = Rett.Altezza + 100

def AumentaRettangolo(Rett, AumentoLargh,AumentoAlt):
    Rett.Larghezza = Rett.Larghezza + AumentoLargh
    Rett.Altezza = Rett.Altezza + AumentoAlt

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

