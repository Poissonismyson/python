
def A_Ex3(nomefile):
    f = open(nomefile,"r")

    for riga in f:
        vuoto = False
        riga = riga.strip() #levamo \n
        if riga == "Prodotto,Importo unitario,Quantità":
            continue
        lista = riga.strip(';')
        importounitario = lista[1]
        quantita = lista[2]
        tot = tot + float(importounitario)*float(quantita)
    
    if vuoto is True:
        return None

    else:
        return round(tot)
    

close()