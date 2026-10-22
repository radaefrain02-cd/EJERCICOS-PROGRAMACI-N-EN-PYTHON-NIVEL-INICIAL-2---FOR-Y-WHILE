"""Cálculo de factorial: Solicita un número entero positivo al usuario y 
calcula su factorial utilizando un contador y un bucle while."""

numero = int(input("Escribe un numero: "))
factorial = 1

while numero > 0:
    factorial = factorial * numero
    numero -= 1
print (f"La factorial es {factorial}")
