"""Contar vocales: Recorre una frase ingresada por el usuario y cuenta cuántas vocales
contiene en total.Ejercicios con bucle while"""

frase = input("Ingresa una frase: ")

contador = 0
i = 0

#len sirve para medir la longitud de algo
while i < len(frase):
    letra = frase[i]
    
    if letra in "aeiouAEIOU":
       contador +=1
    i += 1

print(f"Numero de vocales es: {contador}")