numeros = [1, 2, 3, 4, 5]
# Comprensión de lista con ternario: asigna "par" si n es par, "impar" en caso contrario
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar']