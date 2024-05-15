def contaParole(frasi):
    diz = {}
    rem = set()
    for i in frasi:
        parole = i.split(' ')
        for parola in parole:
            if parola in diz:
                diz[parola] += 1
                rem.discard(parola)
           
            else:
                diz[parola] = 1
                rem.add(parola)

    
    for j in list(rem):
        del diz[j]

    return diz
            

