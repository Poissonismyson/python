def dfs(g, sorgente):
    pila = [sorgente]
    visitati = []

    while len(pila) > 0:
        v = pila.pop(-1)
        if v not in visitati:
            visitati.append(v)
        for vicino in g.getVertex(v).getConnections():
            if vicino not in pila and vicino not in visitati:
                pila.append(vicino)
    return visitati



