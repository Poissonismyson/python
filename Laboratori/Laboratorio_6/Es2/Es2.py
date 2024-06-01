#Definire la classe Gatto nel file Es2.py il cui costruttore prende come parametro il nome di un gatto.
#Realizzare il metodo miagola() che stampa a schermo “nome: Miao!”, dove nome è il nome del gatto scelto
#dall’utente.
#Dopo la definizione della classe creare una nuova istanza di Gatto e chiamare il metodo miagola().

class Gatto:

    def __init__(self,nome): 
        self.nome = nome

    def miagola(self):
        print(self.nome + ": Miao!")
        pass

mario = Gatto("Mario")
mario.miagola()
