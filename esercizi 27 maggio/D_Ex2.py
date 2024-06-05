def D_Ex1(l1,l2):
    l3 = []
    if l1 == [] or l2 == []
        return l3
    else:
        for w in l2:
            for s in l1:
                if w.endswith(s):
                    if s not in l3:
                        l3.append(s)
    l3.sort()                    
    return l3
