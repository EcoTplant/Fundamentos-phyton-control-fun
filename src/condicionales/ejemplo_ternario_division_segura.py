dividendo = 10
divisor = 0
# El ternario evita la división si divisor es cero (cortocircuito de evaluación)
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)