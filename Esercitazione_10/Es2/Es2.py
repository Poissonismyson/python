def maxInDegree(g):
    max = 0
    t = tuple()

    for i in g.getVertices():
            grado = 0
            for j in g.getVertices():
                if i in g.getVertex(j).getConnections():
                    grado += 1
            if grado > max:
                max = grado
                t = (i, max)
    return t

