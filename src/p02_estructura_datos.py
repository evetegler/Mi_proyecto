"""
Estructura de datos en Python
Autor: Evetegler
"""

print("Estructura de datos")
print("------------\n")


# listas
print("Listas")
print("------------")

# índice: 0, 1, 2, 3
fullstack = ["Python", "JavaScript", "HTML", "CSS"]
print(fullstack)
print(type(fullstack))

# acceder a un elemento
print(fullstack[0])  # JavaScript
print(fullstack[-1])  # último elemento
print(fullstack[2])  # HTML

# Una lista de listas
simulando_la_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(simulando_la_matriz)

# tuplas
titulo = "Tuplas (tuples) esto es un ejemplo de repetir caracteres"
print(titulo)
print("-" * len(titulo))

curso = ("Bootcamp", "Fullstack", "Python", "2026")
print(curso)
print(type(curso))

#acceder a valor de la tupla
print(curso[1])  

#cambiar valores en tuplas
#Las tuplas son inmutables, no se pueden cambiar sus valores una vez creadas.

#Curiosidades de ciencias de la computación
#Una cadena de texto se compone como una lista
nombre = "Evetegler"
print(type(nombre), nombre[3])

#Set
titulo = "Set (sets)"
print(titulo)
print("-" * len(titulo))

lenguajes = {"Python", "JavaScript", "HTML", "CSS"}

print(lenguajes)

print( f"El tipo de dato es: {type(lenguajes)}")

listas_duplicadas = ["Python", "JavaScript", "HTML", "CSS", "Python", "JavaScript"]
print(set(listas_duplicadas))




