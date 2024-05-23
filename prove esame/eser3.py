
def perfetto(n):
    if n == 0:
        return False
    divisori = []
    for i in range(1,n):
        if n % i == 0:
            divisori.append(i)
    return sum(divisori) == n

def B_Ex3(nomefile):
    count = 0
    file = open(nomefile, "r")
    testo = file.read().split()
    if(len(testo) == 0):
        return count
    for n in testo:
        if perfetto(n):
            count += 1
    return count