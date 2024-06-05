
def B_Ex2(m1,m2):
    m3 = []
    num_rows_m1 = len(m1)
    num_rows_m2 = len(m2)

    if num_rows_m1 > num_rows_m2:
        for i in range(len(m1)-1,len(m2)-1,-1):
            del m1[i]
    elif num_rows_m2 > num_rows_m1:
        for i in range(len(m2)-1,len(m1)-1,-1):
            del m2[i]
    
    for i in range(len(m1)):
        riga = []
        for j in range(len(m1[i])):
            if m1[i][j] < m2[i][j]:
                riga.append(m1[i][j] + m2[i][j])
            else:
                riga.append(m1[i][j] % m2[i][j])
        m3.append(riga)
    
    return m3
            









'''
    print(m1)
    print(m2)

m1 = [[1,3,2],[2,3,4],[10,5,5]]         # M1 = 3    N=3
m2 = [[7,3,2],[4,5,3]]                  # M2 = 2    N=3

B_Ex2(m1,m2)

'''

           





