def calcolaPuntiPartite(file, giocatore):
    punteggi_giocatori = {}
    f = open(file,"r")
    for riga in f:
        giocatori_e_punteggio = riga.rstrip().split(';')
        for player in giocatori_e_punteggio:
            giocatore_singolo_e_punteggio = player.split()
            if giocatore_singolo_e_punteggio[0] not in punteggi_giocatori:
                punteggi_giocatori[giocatore_singolo_e_punteggio[0]] = int(giocatore_singolo_e_punteggio[1])
            else:
                punteggi_giocatori[giocatore_singolo_e_punteggio[0]] += int(giocatore_singolo_e_punteggio[1])
    
    if giocatore not in punteggi_giocatori:
        return 0
    else:
        return punteggi_giocatori[giocatore]
        

