def restituiscitupla(l,i):
        lista = []
        for el in range(i,len(l)):
                lista.append(l[el])
        
        return tuple(lista)
