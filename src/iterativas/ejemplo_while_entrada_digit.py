entrada = ""
# Repite hasta que el usuario introduzca un número
while not entrada.isdigit():
    entrada = input("Introduce un número: ")
print(f"Has introducido el número: {entrada}")
