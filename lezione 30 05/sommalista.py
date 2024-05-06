
#Ricorsione

def somma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somma(lista[1:len(lista)])
    
a = [1,2,3,4,5]

def IsPower(a,m):
    if a == m:
        return True
    else:
        return a%m == 0 and IsPower(a/m, m)

