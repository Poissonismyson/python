def maxInDegree(g):
    nodo_max = None
    grado_max = 0
    vertici = g.getVertices()
    for v in vertici:
        grado = 0
        for w in vertici:
            w =  g.getVertex(w)
            if v in w.getConnections():
                grado += 1
        if grado > grado_max:
            grado_max = grado
            nodo_max = g.getVertex(v).getId()
       


    return (nodo_max,grado_max)
