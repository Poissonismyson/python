def validamatrice(l):
        lunghezza = len(l[0])
        for i in range(len(l)):
                if len(l[i]) != lunghezza:
                        return False
        return True