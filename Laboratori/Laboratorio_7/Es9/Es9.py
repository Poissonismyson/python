def matriceSparsa(m):
        dic = {}
        for i in range(len(m)):
                for j in range(len(m[i])):
                        if m[i][j] != 0:
                                key =str(i) + ',' + str(j)
                                val = m[i][j]
                                dic[key]=val

        return dic
