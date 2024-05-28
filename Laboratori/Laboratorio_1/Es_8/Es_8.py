importo = int(input("inserire un importo: "))
sconto = int(input("inserire lo sconto: "))
sconto = sconto * 0.01
print("l'importo scontato è pari a ", int(importo * (1-sconto)))