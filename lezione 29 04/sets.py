'''

'''

x = {'alice','bob','carol'}


print(x)

my_set = set('abc')
my_set2 = {'a','b','c'}

print(my_set)
print(my_set2)

#set1 = set(5) non funziona
set2 = {5}

#print(set1 == set2) #False

## Unione di due sets

aset = {11,22,33}
bset = {12,23,33}

cset = aset | bset

print(cset)

dset = {2,4}

dset.union(cset)

print(dset)

print(aset ^ bset) 


