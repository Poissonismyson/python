def minmax(file):
    f = open(file, "r")
    testo = f.read()

    numeri = [int(num) for num in testo.split()]
    if not numeri:
        return ()
    else:
        numeri.sort()
        return (numeri[0], numeri[-1])
