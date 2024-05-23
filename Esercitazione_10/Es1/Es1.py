
def contaArchi(g):
    archi = 0

    for vertex in g.getVertices():

        archi += len(g.getVertex(vertex).getConnections())
    return archi