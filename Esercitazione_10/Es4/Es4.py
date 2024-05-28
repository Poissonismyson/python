
def concatenaRaggiungibili(g, u):
    
    if u not in g:
        return None
    
    def bfs(g, sorgente):
        queue = [sorgente]
        visitati = set()
        while queue:
            v = queue.pop(0)
            if v not in visitati:
                visitati.add(v)
                for vicino in g.getVertex(v).getConnections():
                    if vicino not in visitati:
                        queue.append(vicino)
        return visitati
    
    if u in g:
        ris =  list(bfs(g,u))
        
        ris1 = [int(n) for n in ris]
        ris1.sort()

        s = "".join(str(el) for el in ris1)
        
    
        return s




                 
    
    
    
   
