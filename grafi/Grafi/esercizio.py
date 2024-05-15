
def bfs(g,u):
    davisitare = [u]
    visitati = []
    while len(davisitare) > 0:
        v = davisitare.pop(0) # estraiamo il primo elemento della lista
        if v not in visitati:
            visitati.append(v)
        for vicino in g.getVertex(v).getConnections():
            if (vicino not in visitati) and (vicino not in davisitare):
                davisitare.append(vicino)
    return visitati
def A_ex4(g,u):
    if u not in g.getVertices():
        return None
    raggiungibili = bfs(g,u) # lista dei nodi raggiungibili da u
    #print(raggiungibili)
    s = set(raggiungibili)
    for elem in raggiungibili:
        if int(elem)%2 == 0:
            s.add(int(elem))
    return s