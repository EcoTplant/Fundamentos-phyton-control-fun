# Las funciones son ciudadanos de primera clase
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Asignar función a una variable
convertir = celsius_a_fahrenheit
temperatura_f = convertir(25)  # Equivalente a celsius_a_fahrenheit(25)
print(f"25°C equivalen a {temperatura_f}°F")  # 77.0°F
