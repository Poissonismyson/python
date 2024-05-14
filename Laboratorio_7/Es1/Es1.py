def creaDizionario(n):
    dizionario = {}
    for i in range(n+1):
        dizionario[str(i)] = i**2

    return dizionario
