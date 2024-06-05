def from_ConteaBaggins_to_MonteFato(g):
    vertici = g.getVertices()
    nodo_contea_baggins = None
    
    for v in vertici:
        if g.getVertex(v).getId() == 'ConteaBaggins':
            nodo_contea_baggins = v
    
    raggiungibili_da_contea = dfs(g,nodo_contea_baggins)

    return 'MonteFato' in raggiungibili_da_contea

def dfs(g,sorgente):
    stack = [sorgente]
    visitati = []
    while stack:
        v = stack.pop()
        if v not in visitati:
            visitati.append(v)
        for neighbor in g.getVertex(v).getConnections():
            if neighbor not in stack and neighbor not in visitati:
                stack.append(neighbor)
    return visitati



