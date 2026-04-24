# Función que devuelve un booleano
def es_par(numero):
    return numero % 2 == 0  # True si es par, False en caso contrario

# Función de conversión de temperatura
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Uso de las funciones
print(es_par(4))          # True
print(es_par(5))          # False
print(celsius_a_fahrenheit(25))  # 77.0
