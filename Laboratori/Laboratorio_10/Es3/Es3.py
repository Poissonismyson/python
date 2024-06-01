def sommaVicini(g, u):
    vicini = []
    vertici = g.getVertices()

    if u not in vertici:
        return None
    
    for v in vertici:
        v = g.getVertex(v)
        if u in v.getConnections():
            vicini.append(int(v.getId()))

    return sum(vicini)
