def contaArchi(g):
    archi = 0
    vertici = g.getVertices()
    for v in vertici:
        vertice = g.getVertex(v)
        for a in vertice.getConnections():
            archi += 1

    return archi
