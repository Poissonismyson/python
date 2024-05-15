
def D_Ex4(g):
    #se il è vuoto la funzione ritorna None
    if len(g.getVertices()) == 0:
        return None
    #se esite uno o più percorsi circolari la funzione ritorna None
    for vertice in g.getVertices():
        if vertice in get.GetVertices(vertice).getConnections():
            return True
    return False

