class LavoraStringa:

    def __init__(self,s):
        self.s = s

    def getS(self):
        
        return self.s

    def stampaStringa(self):

        print(self.getS())

    def stampaACapo(self):
        
        return self.s.replace(" ", "\n")

    def concatenaInCoda(self,st):

        return self.s + st

    def concatenaInTesta(self,st):
       
        return st + self.s

    def primoEUltimoCarattere(self):

        return self.s[0] + self.s[-1]

    def lunghezzaDispari(self):
        
        return len(self.s) % 2 != 0


    def lunghezzaPari(self):
        return not self.lunghezzaDispari

    def sostituisci(self,find,replace):
        replaced = self.s.replace(find, replace)
        return replaced

    def trasformaInTitolo(self):

        return self.s.title()

    def raddoppiaCarattere(self,c):

        return self.s.replace(c,2*c)

    def finisceCon(self,st):
        return self.s.endswith(st)

