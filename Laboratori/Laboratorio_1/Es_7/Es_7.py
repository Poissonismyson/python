analisi = int(input("voto di analisi matematica: "))
geo = int(input("voto di geometria: "))
info = int(input("voto di informatica: "))

print("La media è " + str(round((analisi+geo+info)/3, 1)))