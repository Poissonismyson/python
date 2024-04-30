massimo = 0
f = open('input.txt','r')
for riga in f:
    l = riga.split(',')
    for i in l:
        print(i)
        n = int(i)
        if n >= massimo:
            massimo = n
f.close()
print(massimo)