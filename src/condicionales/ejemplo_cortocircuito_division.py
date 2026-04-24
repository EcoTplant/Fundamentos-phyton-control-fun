dividendo = 10
divisor = 0
# Cortocircuito: primero divisor != 0 es False, entonces no evalúa la división
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")