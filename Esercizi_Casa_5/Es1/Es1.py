class Moto:
        def __init__(self,m,n,t,vMax):
                self.modello = m
                self.nome = n
                self.targa = t
                self.max = int(vMax)
        
        def __gt__(self, other):
                return self.max > other.max
        
        def __let__(self,other):
                return self.max <
        


        
      
        pass

m1 = Moto("piaggio","medley","EE129", 110)
m2 = Moto("piaggio","liberty","EE130", 100)
print(m1>m2)
print(m1<m2)

##DEVE RESTITUIRE
## piaggio, medley, EE129, 110
## piaggio, liberty, EE130, 100
                        
