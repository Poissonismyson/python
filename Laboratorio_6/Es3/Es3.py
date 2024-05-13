#Definire la classe Persona nel file Es3.py il cui costruttore prende come parametro due stringhe nome e
#cognome che rappresentano rispettivamente il nome ed il cognome di una persona. Realizzare il metodo
#print NomeCognome() che stampa a schermo il valore dei due attributi.
#Dopo la definizione della classe creare una nuova istanza di Persona e chiamare il metodo printNomeCognome().

class Persona:

    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome


    def printNomeCognome(self):
        print(f"nome: {Persona.nome}\ncognome: {Persona.cognome}")

susanna = Persona("Susanna","Blasi")

susanna.printNomeCognome()
 
