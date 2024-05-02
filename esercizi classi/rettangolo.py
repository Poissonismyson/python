class Punto():
    pass

class Rettangolo():
    pass

def StampaPunto(P):
    print('(' + str(P.x) + ',' + str(P.y) + ')')

def TrovaCentro(Rettangolo):
    P = Punto()
    P.x = Rettangolo.BassoSinistra.x + Rettangolo.larghezza/2
    P.y = Rettangolo.BassoSinistra.y + Rettangolo.Altezza/2
    return P
