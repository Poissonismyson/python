#Scrivere una funzione ricorsiva somma(n1, n2) che prende come paramentri due interi n1 e n2 e restituisce
#la somma di tutti gli interi compresi tra n1 e n2.

def somma(n1,n2):
    
    if n1 == n2:
        return n1
    
    return n1 + somma(n1+1,n2)

print(somma(5,10))




def sottrazione(n1,n2):

    if n1 == n2:
        return -n1
    
    return -n1 + sottrazione(n1+1,n2)
