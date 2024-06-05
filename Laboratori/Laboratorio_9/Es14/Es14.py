def multipliDecrescenti(l):
    if len(l) == 0:
        return []
    if l[0]%10 == 0:
        return multipliDecrescenti(l[1:]) + [l[0]]
    else:
        return multipliDecrescenti(l[1:])
    
