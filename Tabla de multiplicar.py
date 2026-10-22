"""Tabla de multiplicar: Dado un número entero, 
imprime su tabla de multiplicar del 1 al 10 utilizando un bucle for."""

numero = int(input("Escribe un numero: "))

for i in range (1,11):
    multi = numero * i
    print (f"{numero} * {i} = {multi}")
