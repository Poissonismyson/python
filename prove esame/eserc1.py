
def A_Ex1(l1,l2):
    if len(l1) == 0 or len(l2) == 0:
        return []
    risultato = []
    for elem1 in l1:
        for elem2 in l2:
            if elem1 in elem2:
                risultato.append(elem2)
    s = set(risultato)
    l = list(s)
    l.sort()
    return l



