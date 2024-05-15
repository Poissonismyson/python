def contaArchi(g):
    
    archi = 0

    for node in g.getVertices():
        archi += len(g.getVertex(node).getConnections())
    
    return archi
        