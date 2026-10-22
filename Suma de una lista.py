"""Suma de una lista: Dada una lista de números enteros,
calcula y muestra la suma total de sus elementos utilizando for."""

numeros = [1,2,3,4,5,6]

total = 0

for n in numeros:
    total += n

print (f"La suma de numeros es {total}")