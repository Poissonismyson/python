
class Dog:
    
    scientific_name = 'Canis lupus familiaris'

    def __init__(self, name):
        self.name = name

rex = Dog('Rex')
fido = Dog('Fido')

my_string = "hello"
slice_from_end = my_string[0:7]
print(slice_from_end)