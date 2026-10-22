"""Suma hasta número negativo: Pide números al usuario de forma repetida hasta
que introduzca un número negativo, momento en el cual el bucle terminará 
y mostrará la suma acumulada de los valores ingresados."""

print ("Se sumaran todos los numeros que coloque! Introduzca un numero negativo para ver el resultado.")
numero = int(input("Ingrese su primer numero: 8"))
suma = 0

while numero > 0:
    suma += numero
    numero = int(input("Introduce otro numero: "))             
print (f"La suma total seria: {suma}")