def dividir_seguro(a, b):
    if b == 0:
        print("Error: División por cero")
        return None  # Salida anticipada
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))   # 5.0
print(dividir_seguro(10, 0))   # Error y luego None
