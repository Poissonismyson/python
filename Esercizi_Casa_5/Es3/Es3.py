class Moto:
        #COMPLETARE
        pass


def Es3(l):
        #COMPLETARE
        return None


m1 = Moto("piaggio","medley","EE129", 110)
m2 = Moto("piaggio","liberty","EE130", 100)
m3 = Moto("aprilia","scarabeo","CE111", 45)
m4 = Moto("honda","sh","DD111", 115)
m5 = Moto("suzuki","gs","AD111", 250)
l1 = [m1,m2,m3,m4,m5]
print(Es3(l1))


m6 = Moto("aprilia","scarabeo","AE111", 45)
m7 = Moto("aprilia","scarabeo","AA111", 45)
m8 = Moto("honda","sh","ZZD111", 115)
m9 = Moto("suzuki","gs","AD111", 250)
l2 = [m6,m7,m8,m9]
print(Es3(l2))

## DEVE STAMPARE
## suzuki, gs, AD111, 250
## aprilia, scarabeo, AA111, 45
