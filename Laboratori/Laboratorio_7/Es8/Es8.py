def convertiData(t):
        giorno = {
                 1: "primo", 2: "secondo", 3: "terzo", 4: "quarto", 5: "quinto",
                6: "sesto", 7: "settimo", 8: "ottavo", 9: "nono", 10: "decimo",
                11: "undicesimo", 12: "dodicesimo", 13: "tredicesimo", 14: "quattordicesimo",
                15: "quindicesimo", 16: "sedicesimo", 17: "diciassettesimo", 18: "diciottesimo",
                19: "diciannovesimo", 20: "ventesimo", 21: "ventunesimo", 22: "ventiduesimo",
                23: "ventitreesimo", 24: "ventiquattresimo", 25: "venticinquesimo", 26: "ventiseiesimo",
                27: "ventisettesimo", 28: "ventottesimo", 29: "ventinovesimo", 30: "trentesimo",
                31: "trentunesimo"}

        mese = {
                1: 'Gennaio', 2: 'Febbraio', 3: 'Marzo', 4: 'Aprile', 5: 'Maggio', 6: 'Giugno',
                7: 'Luglio', 8: 'Agosto', 9: 'Settembre', 10: 'Ottobre', 11: 'Novembre', 12: 'Dicembre'
                }
        
        l = list(t)


        return (giorno[l[0]], mese[l[1]], l[2])
