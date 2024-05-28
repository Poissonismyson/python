serie = input("inserire il nome della serie: ")
numero = int(input('inserire il numero di puntate viste: '))
lunghezza = int(input('inserire la durata media di una puntata (in minuti): '))

print(f"Hai visto {round(numero*lunghezza/60,1)}h di {serie.title()}.")