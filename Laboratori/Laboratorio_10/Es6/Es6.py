def maxOutDegree(g):
    maximo = None
    vicini_di_maximo = 0

    for v in g.getVertices():
        conta_vicini = 0
        for vicino in g.getVertex(v).getConnections():
            conta_vicini +=1
        if conta_vicini > vicini_di_maximo:
            vicini_di_maximo = conta_vicini
            maximo =  g.getVertex(v).getId()




    return (maximo, vicini_di_maximo)
