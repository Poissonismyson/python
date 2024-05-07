
def Fattoriale(n):
    if n <= 1:
        return 1
    else:
        return n * Fattoriale(n-1)
