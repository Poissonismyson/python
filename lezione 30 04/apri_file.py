f = open("input.txt","r")
#riga = f.readline()
#print(riga.strip())
#while riga != "":
#    riga = f.readline().strip()
#    print(riga.strip())

lista = f.readlines()
i = 0
while i < len(lista):
    elem = lista[i].strip()
    lista[i] = elem
    i += 1
f.close()

'''
with open("input.txt","r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

for line in lines:
    print(line)
'''
