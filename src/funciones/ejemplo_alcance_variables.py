# Variables dentro de una función tienen alcance local
def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)   # Variable local
    precio_final = precio - descuento         # Variable local
    return precio_final

precio_con_descuento = calcular_descuento(100)
print(f"Precio con descuento: {precio_con_descuento}")  # 90.0

# La siguiente línea daría error porque 'descuento' no existe fuera de la función
# print(descuento)  # NameError
