def bfs(g, sorgente):
    coda = [sorgente]
    visitati = []

    while len(coda) > 0:
        v = coda.pop(0)
        if v not in visitati:
            visitati.append(v)
        for vicino in g.getVertex(v).getConnections():
            if vicino not in coda and vicino not in visitati:
                coda.append(vicino)
    return visitati







