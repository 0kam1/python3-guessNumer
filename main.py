import random

numeroIntentos = 0
numeroMinimo = 1
numeroMaximo = 20

print("Hola, cual es tu nombre?: ")
usuario = input()

numero = random.randint(numeroMinimo, numeroMaximo)
print("Ok, " + usuario + '. Estoy pensando en un numero entre '+ str(numeroMinimo) + ' y ' + str(numeroMaximo))

while numeroIntentos < 6:
    print("Dime un numero: ")
    guess = input()
    guess = int(guess)

    numeroIntentos = numeroIntentos + 1

    if guess < numero:
        print("Tu numero es demasiado bajo")
    if guess > numero:
        print("Tu numero es demasiado alto")
    if guess == numero:
        print("Bien hecho " + usuario + ' adivinaste mi numero en ' + str(numeroIntentos) + ' intentos.')
        break

if guess != numero:
    print("No, el numero en el que estaba pensando era " + str(numero))