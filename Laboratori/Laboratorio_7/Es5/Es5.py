def riassumiOrdini(ordini):
    diz = {}

    for i in ordini:
        ordine = i.split(',')
        if ordine[1] == 'Pizza' and int(ordine[3]) >0:
            if ordine[2] not in diz:
                diz[ordine[2]] = int(ordine[3])
            else:
                diz[ordine[2]] += int(ordine[3])
    return diz
