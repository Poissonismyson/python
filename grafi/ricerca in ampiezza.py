
def bfs (g,sorgente):
    coda = [sorgente]
    visitati = []
    while len(coda) > 0:
        v = coda.pop(0)
        if v not in visitati:
            visitati.append(v)
            for vicino in g.getVertex().getConnections():
                if (vicino not in visitati) and (vicino not in coda):
                    coda.append(vicino)
    return visitati