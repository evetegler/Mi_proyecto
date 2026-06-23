numero1 = input("Ingrese el primer número entero: ")

# Validar que sea número entero positivo
while not numero1.isdigit():
    numero1 = input("Error. Ingrese un número entero válido: ")

numero2 = input("Ingrese el segundo número entero: ")

while not numero2.isdigit():
    numero2 = input("Error. Ingrese un número entero válido: ")

suma = int(numero1) + int(numero2)
print("La suma de", numero1, "y", numero2, "es:", suma)
