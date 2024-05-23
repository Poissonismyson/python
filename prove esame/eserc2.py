
def prodotto(l):
    prod = 1
    for stringa in l:
        for carattere in stringa:
            prod = prod * ord(carattere)
    return prod


def A_Ex2(m1,l2):
    m2 = []
    prod = prodotto(l2)
    for riga in m1:
        somma = sum(riga)
        if somma > prod:
            m2.append(riga)
        else:
            riga.reverse()
            m2.append(riga)
    return m2

