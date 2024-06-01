def spaceCraft(navicelle):

        dic = {}
        lo = []
        lc = []

        for n in navicelle:
                l = n.split(',')
                
                if l[0] == 'Lato Oscuro':
                        lo.append(l)
                else:
                        lc.append(l)

        lo = powersort(lo)
        lc = powersort(lc)
        lo1 =[]
        lc1 = []
        if lo:
                for i in lo:
                        p = (i[2],i[1])
                        lo1.append(p)
        if lc:
                for i in lc:
                        p = (i[2],i[1])
                        lc1.append(p)
        
        if lo1:
                dic['Lato Oscuro'] = lo1
        
        if lc1:
                dic['Lato Chiaro'] = lc1
        

        return dic



def powersort(l):
        ret = []
        
        while l:
                max_index = 0
                for i in range(1,len(l)):
                        if int(l[i][3]) > int(l[max_index][3]):
                                max_index = i
                
                ret.append(l.pop(max_index))