class Persona :

    def __init__(self, nome, cognome): 
        self.nome = nome
        self.cognome = cognome


    def printNomeCognome(self):
        print(self.nome + " " + self.cognome)


class Automobile :

    def __init__(self,t,m,c,p):
        self.t = t
        self.m= m
        self.c = c
        self.p = p


    def printAutomobile(self):
        print(f"{self.t}\t{self.m}\t{self.c}\t{self.p.nome}\t{self.p.cognome}")
  
    
    def verniciatura(self,nuovoColore):
        self.c = nuovoColore


    def cambiaProprietario(self,nuovoProprietario):
        self.p = nuovoProprietario

p1 = Persona("Camillo", "Benzo")

p2 = Persona("Giovanni", "Almond")

car = Automobile("AA123AA", "Land Rover", "Nero", p1)

car.printAutomobile()
car.verniciatura("Verde")
car.cambiaProprietario(p2)
car.printAutomobile()






