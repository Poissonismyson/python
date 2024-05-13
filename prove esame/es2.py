
def A_Ex2(m):
    matOutput = []
    for i in range(len(m)):
        riga = []
        for j in range(len(m[i])):
            k = m [i] [j]
            if k <= 0:
                riga.append(0)
            else:
                somma = 0
                for p in range(j+1,k+1): #range (1,k+1)
                    if j+p < len(m[i]):
                        somma += m[i][p] #m [i] [p+j]
                    else:
                        break
                riga.append(somma)    
        matOutput.append(riga)
    return matOutput

