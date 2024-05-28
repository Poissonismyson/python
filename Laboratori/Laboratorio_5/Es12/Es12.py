def scambiacolonne(m,i1,i2):
    if not m:
        return m
    
    lunghezza = len(m[0])
    for i in range(len(m)):
        if len(m[i]) != lunghezza:
            return m

    m1 = []

    for i in range(len(m)):
        riga = []
        for j in range(len(m[i])):
            if j == i1:
                riga.append(m[i][i2])
            elif j == i2:
                riga.append(m[i][i1])
            else:
                riga.append(m[i][j])
        m1.append(riga)

    return m1            

