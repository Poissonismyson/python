def sommaVicini(g, u):
    
    if u not in g.getVertices():
        return None
    
     s = 0
    
    for vertexname in g.getVertices():
        if u in g.getVertex(vertexname).getConnections():
            s += int(vertexname)
    return s
