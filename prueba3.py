"""Pide dos números decimales al usuario - Ya
Realiza operaciones básicas como suma, resta, multiplicación
y división.  - Ya
Muestra los resultados en pantalla, con la división 
mostrando solo 2 decimales.
"""
numero1 = int(input("Digita el primer número: "))
numero2 = int(input("Digita el segundo número: "))     
#  Realiza operaciones básicas como suma, resta, multiplicación
# y división. 
suma = numero1 + numero2 
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")
print(f"El resultado de la division es: {division}")