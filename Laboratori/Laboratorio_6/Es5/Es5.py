class Personaggio:

    def __init__(self,n,i,f,m): 
        self.nome = n
        self.intelligenza = i
        self.forza = f
        self.magia = m

    
    def piuForte(self,p):
        self.abilita = (self.intelligenza + self.forza + self.magia)/3
        p.abilita = (p.intelligenza + p.forza + p.magia)/3
        if self.abilita >= p.abilita:
            return str(self)
        else:
            return str(p)

    def __str__(self):
        ret = self.nome+":\n"
        ret+=str(1)+")Intelligenza: "+str(self.intelligenza)+"\n"
        ret+=str(2)+")Forza: "+str(self.forza)+"\n"
        ret+=str(3)+")Magia: "+str(self.magia)
        return ret

