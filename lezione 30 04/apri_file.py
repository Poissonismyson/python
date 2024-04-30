f = open("input.txt","r")
riga = f.readline()
print(riga.strip())
while riga != "":
    riga = f.readline().strip()
    print(riga.strip())

lista = f.readlines()
i = 0
while i < len(lista):
    elem = lista[i].strip()
    lista[i] = elem
    i += 1
