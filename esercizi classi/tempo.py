
class Tempo:
    pass

Time = Tempo()
Time.Ore = 11
Time.Minuti = 59
Time.Secondi = 30

def StampaTempo(Orario):
    print(str(Orario.Ore) + ":" + str(Orario.Minuti) + ":" + str(Orario.Secondi))


class Tempo:
    def StampaTempo(Orario):
        print(str(Orario.Ore) + ":" + str(Orario.Minuti) + ":" + str(Orario.Secondi))

OraAttuale = Tempo()
OraAttuale.Ore = 9
OraAttuale.Minuti = 14
OraAttuale.Secondi = 30
StampaTempo(OraAttuale)

class Tempo:
    def StampaTempo(Orario):
        print(str(Orario.Ore) + ":" + str(Orario.Minuti) + ":" + str(Orario.Secondi))
    def Dopo(self, Tempo2):
        if self.Ore > Tempo2.Ore:
            return True
        if self.Ore < Tempo2.Ore:
            return False
        if self.Minuti > Tempo2.Minuti:
            return True
        if self.Minuti < Tempo2.Minuti:
            return False
        if self.Secondi > Tempo2.Secondi:
            return True
        return False
t = Tempo()
t.Ore = 10 
t.Minuti = 30
t.Secondi = 10
t1 = Tempo()
t1.Ore = 10
t1.Minuti = 30 
t1.Secondi = 15
print(t.Dopo(t1))
t.StampaTempo()
t1.StampaTempo()

class Tempo:
    def __init__(self, Ore=0, Minuti=0, Secondi=0):
        self.Ore = Ore
        self.Minuti = Minuti
        self.Secondi = Secondi
    def StampaTempo(self):
        print(str(self.Ore) + ":" + str(self.Minuti) + ":" + str(self.Secondi))
    def __str__(self):
        return str(self.Ore) + ":" + str(self.Minuti) + ":" + str(self.Secondi)
OraAttuale = Tempo(9, 14, 30)
OraAttuale.StampaTempo()

OraAttuale = Tempo(9)
OraAttuale.StampaTempo()

OraAttuale = Tempo(9, 14)
OraAttuale.StampaTempo()

OraAttuale = Tempo(Secondi=30, Ore=9)
OraAttuale.StampaTempo()


InizioLezione = Tempo(9)
print(str(InizioLezione))

