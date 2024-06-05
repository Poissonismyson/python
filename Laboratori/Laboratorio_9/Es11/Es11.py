def massimo(l):
    if len(l) == 0:
        return 0
    
    if len(l) == 1:
        return l[0]
    
    else:
        return max(l[0], massimo(l[1:]))
