class Moto:
        #COMPLETARE
        pass

def Es7(l):
        return None

m1 = Moto("piaggio","medley","EE129", 110)
m2 = Moto("honda","sh","EG129", 110)
m3 = Moto("honda","africa twin","GG130", 100)
m4 = Moto("suzuki","tc12","EE161", 110)

for elem in Es7([m1,m4]):
        print(elem)
print()
for elem in Es7([m1,m2,m3]):
        print(elem)
        
#DEVE RESTITUIRE
## piaggio, medley, EE129, 110, 8
## suzuki, tc12, EE161, 110, 2
##
## honda, africa twin, GG130, 100, 9        
## honda, sh, EG129, 110, 9
## piaggio, medley, EE129, 110, 8



