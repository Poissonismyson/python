class LavoraLista:

    def __init__(self,l):
<<<<<<< HEAD
        self.l = l


    def listaFormattata(self): 
        ret = ""
        for i in range(len(self.l)):
            ret += ( str(i+1) + " => " + str(self.l[i]) + "\n" )
        return ret.strip('\n')


    def stampaListaFormattata(self):
        
        print(self.listaFormattata())

    def elementoIesimo(self,i):
        
        return self.l[i]

    def stampaPrimoEUltimo(self):
        ret = str(self.l[0]) + str(self.l[-1])
        return ret
    
    def inversoLista(self):
        linv = self.l[::-1]
        return linv

    def sommaLista(self):
        n = sum(self.l)
        return n

    def sommaNumeriPari(self):
        pari = []
        for i in self.l:
            if i % 2 == 0:
                pari.append(i)
        return sum(pari)

                
    def sommaNumeriDispari(self):
        
        return sum(i for i in self.l if i%2 != 0 )

    def sommaListaIsDispari(self):
        
        return self.sommaLista() %2 != 0

    def sommaListaIsPari(self):

        return not self.sommaListaIsDispari()
        
    def creaMatriceRipetizioni(self,n):
        m = []
        for i in self.l:
            row =[]
            for j in range(n):
                row.append(i)
            m.append(row)
    
        return m
=======
        #da completare a cura dello studente
        pass

    def listaFormattata(self): 
        #da completare a cura dello studente
        return None

    def stampaListaFormattata(self):
        #da completare a cura dello studente
        pass

    def elementoIesimo(self,i):
        #da completare a cura dello studente
        return None

    def stampaPrimoEUltimo(self):
        #da completare a cura dello studente
        pass
    
    def inversoLista(self):
        #da completare a cura dello studente
        return None

    def sommaLista(self):
        #da completare a cura dello studente
        return None

    def sommaNumeriPari(self):
        #da completare a cura dello studente
        return None
                
    def sommaNumeriDispari(self):
        #da completare a cura dello studente
        return None

    def sommaListaIsDispari(self):
        #da completare a cura dello studente
        return None

    def sommaListaIsPari(self):
        #da completare a cura dello studente
        return None
        
    def creaMatriceRipetizioni(self,n):
        #da completare a cura dello studente
        return None
>>>>>>> 1a3d7b98b999b4e56004ea7967e618092a76fbf2
