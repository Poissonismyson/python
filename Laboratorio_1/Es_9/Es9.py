nomeSerieTv = str(input("inserire nome serie Tv: "))
numeroEpisodiVisti = int(input("inserire numero episodi visti: "))
lunghezzaMediaEpisodio = int(input("inserire lunghezza media episodio in minuti: "))
totaleOreViste = (numeroEpisodiVisti * lunghezzaMediaEpisodio)/60
totaleOreViste=round(totaleOreViste,1)
print("Hai visto ", totaleOreViste, "h di ", nomeSerieTv)
 
