def maxInDegree(g):
    t = tuple()
    massimo = 0
    for v1 in g.getVertices():
        grado = 0
        for v2 in g.getVertices():
            if v1 in g.getVertex(v2).getConnections():
                grado += 1
            if grado > massimo:
                massimo = grado
                t = (v1,massimo)
            
    return t

