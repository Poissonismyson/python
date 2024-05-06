
def Potenza(x,p):
    if p == 0:
        return 1
    else:
        return x * Potenza(x,p-1)
