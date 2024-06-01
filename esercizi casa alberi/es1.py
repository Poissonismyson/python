#Scrivere una funzione ricorsiva operazione(list input) che prende come paramentro una lista di numeri e
#restituisce il risultato della somma di tutti i numeri pari e la sottrazione di tutti i numeri dispari

def operazione(l):
    if l == []:
        return 0
    else:
        if l[0] % 2 == 0:
            return l[0] + operazione(l[1:])
        else:
            return -l[0] + operazione(l[1:])
        


l = [2, 4, 5, 3, 8, 1]
print(operazione(l))