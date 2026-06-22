print ("Hola Mundo")
print ("Bienvenidos a Python")

"""Este es un comentario de varias lineas
que se puede usar para explicar el codigo o para escribir notas"""
# Este es un comentario de una sola linea
# Variables
nombre = "Evelin"
edad = 40
print ("Mi nombre es", nombre, "y tengo", edad, "años")
# Operaciones matematicas
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
print ("La suma de", a, "y", b, "es", suma)
print ("La resta de", a, "y", b, "es", resta)
print ("La multiplicacion de", a, "y", b, "es", multiplicacion)
print ("La division de", a, "y", b, "es", division)
# Condicionales
if edad >= 18:
    print ("Eres mayor de edad")
else:    print ("Eres menor de edad")
# Bucles
for i in range(5):
    print ("El valor de i es", i)
contador = 0
while contador < 5:
    print ("El valor del contador es", contador)
    contador += 1

print(type(nombre))
print(type(edad))

#metodos en variables
print(nombre.upper())
print(nombre.lower())
print(nombre.capitalize())

#asignar tipo de datos a una variable
numero = int(input("Ingrese un numero: "))
print("El numero ingresado es:", numero)

#cambiar tipo de dato de una variable
numero_str = str(numero)
print("El numero como cadena es:", numero_str)

#posicion de memoria de una variable
print("La posicion de memoria de la variable numero es:", id(numero))

#comportamiento de numeros enteros
print("El numero es:", numero)
print("El numero es:", numero + 10)

#numero de paginas para un libro
paginas = 300
print("El libro tiene", paginas, "paginas")

#saber si un numero es par o impar
if numero % 2 == 0:
    print("El numero es par")
else:    print("El numero es impar")

#comportamiento de cadenas de texto
frase = "Python es un lenguaje de programacion"
print("La frase es:", frase)
print("La frase en mayusculas es:", frase.upper())
print("La frase en minusculas es:", frase.lower())
print("La frase capitalizada es:", frase.capitalize())

#conversion de tipos de datos
numero_float = float(numero)
print("El numero como flotante es:", numero_float)

#trabajando con imput y output
nombre_usuario = input("Ingrese su nombre: ")
print("Hola", nombre_usuario, "bienvenido a Python")

#usando f-strings para formatear texto
print(f"Hola {nombre_usuario}, bienvenido a Python")

#Checklist para GitHub
# - [ ] Crear un repositorio en GitHub
# - [ ] conectar el repositorio local con el remoto
# - [ ] actualizar repositorio remoto con los cambios realizados localmente
# - [ ] crear una nueva rama para trabajar en una nueva funcionalidad
# - [ ] hacer un pull request para fusionar la nueva rama con la rama principal
# - [ ] revisar y aprobar el pull request antes de fusionar
# - [ ] actualizar remoto con los cambios fusionados
# - [ ] hacer merge del pull request para fusionar la nueva rama con la rama principal
# - [ ] actualizar repo local con los cambios fusionados





