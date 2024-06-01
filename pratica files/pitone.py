f = open('input.txt','r')

i = 1
for riga in f:
    riga = riga.rstrip()
    print(i,riga)
    i += 1

f.close()

