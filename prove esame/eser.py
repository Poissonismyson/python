
def B_Ex1(l1,x):
    l2 = []
    for i in range(len(l1)):
        for j in range(len(l1[i])):
            if l1[i][j] == x:
                l2.append((i+1,j+1))
    return l2

def B_Ex2(l1,x):
    l2 = []

    N = len(l1)
    i = 0
    while(i<N):
        M = len(l1[i])
        j = 0

        while(j<M):
            if l1[i][j] == x:
                l2.append((i,j))
            j += 1
        i += 1
    return l2