def concatenaRaggiungibili(g, u):
    
    lista_vicini = dfs(g,u)
    
    lista_vicini.sort(key = int)

    

    return ''.join(lista_vicini)

def dfs(g,u):
    pila = [u]
    visitati = []
    while pila:
        v = pila.pop()
        if v not in visitati:
            visitati.append(v)
        for vicino in g.getVertex(v).getConnections():
            if vicino not in visitati and vicino not in pila:
                pila.append(vicino)
    return visitati


