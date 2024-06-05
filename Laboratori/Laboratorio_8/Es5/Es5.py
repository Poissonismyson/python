def frequenzaCarattere(file, c):
    f = open(file, "r")

    m = []
    for riga in f:
        m.append(riga.strip().split(' '))

    f.close()

    presenze = {}

    for i in range(len(m)):
        for j in range(len(m[i])):
            if c in m[i][j].lower():
                if i not in presenze:
                    presenze[i] = 1
                else:
                    presenze[i] += 1
    print(m)
    print(presenze)

    indice_massimo = -1
    frequenza_massima = -1

    for i in presenze:
        if presenze[i] > frequenza_massima:
            indice_massimo = i
            frequenza_massima = presenze[i]
    
    if not presenze:
        return -1
    

    else:
        return indice_massimo

