#v1.0.0
#Historia de usuario:

"""El usuario necesita calcular el área de un rectángulo, para ello debe ingresar la base y la altura del mismo, y el sistema le devolverá el área calculada."""


base = input("Ingrese la base del rectángulo: ")
altura = input("Ingrese la altura del rectángulo: ")


if base.isdigit() and altura.isdigit():
    area = int(base) * int(altura)
    print(f"El área del rectángulo es: {area}")
else:
    print("Error:", "Los valores deben ser números enteros positivos.")
    print(f"Los valores ingresados fueron: base = {base}, altura = {altura}")
    