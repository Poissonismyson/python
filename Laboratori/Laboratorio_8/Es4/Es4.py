def sommaRighe(file):
    
    f = open(file,"r")
    l = []

    for elem in f:
        elem = map(int, elem.split(';'))
        l.append(sum(elem))
    f.close()

    return l


