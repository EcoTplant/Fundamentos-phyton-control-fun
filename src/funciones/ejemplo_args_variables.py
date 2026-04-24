# *args permite número variable de argumentos posicionales
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(1, 2))           # 3
print(sumar(1, 2, 3, 4, 5))  # 15
print(sumar())                # 0
