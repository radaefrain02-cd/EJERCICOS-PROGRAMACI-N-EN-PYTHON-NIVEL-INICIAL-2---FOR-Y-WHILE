"""Adivinar el número: Crea un programa con un número secreto fijo;
el bucle while debe pedir intentos al usuario 
e indicarle si el número secreto es mayor o menor hasta que acierte."""

secreto = 10

intento = 0

while secreto != intento:
    intento = int(input("Adivina el numero secreto: "))

    if intento < secreto:
        print ("El numero es mayor.")
    elif intento > secreto:
        print ("El numero es menor.")
    else: 
        print ("Lo lograste!")