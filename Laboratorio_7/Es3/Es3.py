def quantePersone(mete):
    diz = {}
    for i in mete:
        lista = i.strip().split(',')
        if len(lista) == 3:
            meta = lista[0].strip()
            mese = lista[1].strip()
            persone = int(lista[2].strip())
            if (mese == 'Luglio' or mese == 'Agosto'):
                if meta not in diz:
                    diz[meta] = persone
                else:
                    diz[meta] += persone
    return diz


