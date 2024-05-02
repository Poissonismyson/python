
class punto:
    pass

p1 = punto()
p2 = punto()

p1.x = 3
p1.y = 4

p2.x = 3
p2.y = 4

print(p1)
print(p2)

print ('(' + str(p1.x) + ',' + str(p1.y) + ')' )
DistanzaAlQuadrato = p1.x **2 + p1.y **2
print(DistanzaAlQuadrato)

def StampaPunto(P):
    print('(' + str(P.x) + ',' + str(P.y) + ')')

class Rettangolo():
    pass

rett = Rettangolo()
rett.larghezza = 100
rett.altezza = 200

rett.BassoSinistra = punto()
rett.BassoSinistra.x = 0
rett.BassoSinistra.x = 0