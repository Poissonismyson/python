def maxOutDegree(g):
    vertici = g.getVertices()
    max = 0
    for vertice in vertici:
        print( vertice.getConnections )
        if (vertice.getConnections()) > max:
            grosso = vertice
    return (grosso, len(grosso.getConnections()))
