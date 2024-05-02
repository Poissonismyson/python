class Punto():
    pass

class Rettangolo():
    pass

def StampaPunto(P):
    return ('(' +str(P.x) + ',' +str(P.y) + ')')

def TrovaCentro(Rettangolo):
    P = Punto()
    P.x = Rettangolo.BassoSinistra.x + Rettangolo.Larghezza/2
    P.y = Rettangolo.BassoSinistra.y + Rettangolo.Altezza/2
    return P


def DistanzaAlQuadrato(P):
    return (int(P.x) * int(P.x) +int(P.y) *int(P.y))
