def verificaLista(l,i):
    if not l:
        return False
    
    if len(l) > 0 and prodotto(l[0]) != i:
        return False
    
    if len(l) > 2:
        return verificaLista(l[2:],i)
    
    return True

   

def prodotto(sl):
    if not sl:
        return 1
    
    return sl[0]*prodotto(sl[1:])
    