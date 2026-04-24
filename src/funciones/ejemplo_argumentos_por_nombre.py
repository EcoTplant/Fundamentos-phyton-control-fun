def dividir(dividendo, divisor):
    return dividendo / divisor

# Argumentos posicionales
resultado1 = dividir(10, 2)     # 5.0

# Argumentos por nombre (orden indistinto)
resultado2 = dividir(divisor=2, dividendo=10)  # 5.0
print(resultado1, resultado2)
