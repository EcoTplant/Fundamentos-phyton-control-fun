def calcular_descuento(precio, porcentaje):
    # Validación de argumentos
    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("El precio debe ser un número positivo")
    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")
    descuento = precio * (porcentaje / 100)
    return precio - descuento

try:
    precio_final = calcular_descuento(100, 15)
    print(f"Precio con descuento: {precio_final}")  # 85.0
    precio_erroneo = calcular_descuento(-50, 10)    # Lanza ValueError
except ValueError as e:
    print(f"Error: {e}")
