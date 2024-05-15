from Grafo import Graph
import BuildGraph

def bfs(g, sorgente):
    coda = [sorgente] #da visitare
    visitati = []
    while len(coda) > 0:
        print(visitati,"|",coda)
        v = coda.pop(0) #estraggo il primo inserito
        if v not in visitati:
            visitati.append(v)
        for vicino in g.getVertex(v).getConnections():
            if (vicino not in visitati) and (vicino not in coda):
                coda.append(vicino)
    print(visitati,"|",coda)
    return visitati

def dfs(g, sorgente):
    pila = [sorgente] #da visitare
    visitati = []
    while len(pila) > 0:
        print(visitati,"|",pila)
        v = pila.pop(-1) #estraggo ultimo inserito
        if v not in visitati:
            visitati.append(v)
        for vicino in g.getVertex(v).getConnections():
            if (vicino not in visitati) and (vicino not in pila):
                pila.append(vicino)
    print(visitati,"|",pila)
    return visitati

    
g = BuildGraph.costruisci_grafo("archi.txt")
v = 'V0'
print("lista dei vertici",g.getVertices())
#for vert in g:
    #print(vert)
for vert in g.getVertices():
    print(g.getVertex(vert))
print()
print("BFS:")
print("nodi visitati da",v+':',bfs(g,v))
print()
print("DFS:")
print("nodi visitati da",v+":",dfs(g,v))



