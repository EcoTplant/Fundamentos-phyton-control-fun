# Función práctica con múltiples returns
def convertir_temperatura(valor, origen, destino):
    """
    Convierte temperatura entre Celsius (C), Fahrenheit (F) y Kelvin (K).
    """
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None
    if origen == destino:
        return valor
    # Convertir a Celsius
    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:  # 'C'
        celsius = valor
    # Convertir desde Celsius
    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:  # 'C'
        return celsius

print(convertir_temperatura(25, 'C', 'F'))   # 77.0
print(convertir_temperatura(98.6, 'F', 'C')) # 37.0
print(convertir_temperatura(0, 'C', 'K'))    # 273.15
print(convertir_temperatura(20, 'X', 'Y'))   # None
