
def Trova(Stringa, Carattere):
    Indice = 0
    while Indice < len(Stringa):
        if Stringa[Indice] == Carattere:
            return Indice
        Indice += 1
    return None

def Trova(Stringa, Carattere, Inizio =0):
    Indice = Inizio
    while Indice < len(Stringa):
        if Stringa[Indice] == Carattere:
            return Indice
        Indice += 1
    return None