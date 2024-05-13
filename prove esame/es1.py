
def A_Ex1(l1,l2):
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i])
        if i < len(l2):
            l3.append(l2[i])
    for j in range (len(l1),len(l2)):
        l3.append(l2[i])
    return l3
