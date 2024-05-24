def sommaVicini(g, u):

    somma = 0

    if u not in g:
        return None
    
    if u in g:
        for v in g.getVertices():
            vertice = g.getVertex(v)
            if u in vertice.getConnections():
                somma += int(vertice.getId())
    
    return somma