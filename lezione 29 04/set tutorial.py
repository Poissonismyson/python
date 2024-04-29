def trova_parole(testo):
    testo = testo.lower()

    punteggiatura = ".,!?:"
    
    for p in punteggiatura:
        testo = testo.replace(p, " ")
    
    parole = set(testo.split())

    return (parole, len(parole))


def trova_parole_ordinate(testo):
    testo = testo.lower()

    punteggiatura = ".,!?:"
    
    for p in punteggiatura:
        testo = testo.replace(p, " ")
    
    parole = set(testo.split())

    parole_ordinate = sorted(parole)
    return (parole_ordinate, len(parole_ordinate))

print(trova_parole_ordinate("The quick quick brown fox jumps over the lazy dog!"))
print(trova_parole_ordinate("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\
                            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\
                            proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))

