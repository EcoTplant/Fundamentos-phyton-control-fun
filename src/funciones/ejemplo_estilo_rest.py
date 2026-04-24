def convertir_a_celsius(fahrenheit):
    """
    Convierte una temperatura de Fahrenheit a Celsius.

    :param fahrenheit: Temperatura en grados Fahrenheit
    :type fahrenheit: float
    :return: Temperatura en grados Celsius
    :rtype: float
    """
    return (fahrenheit - 32) * 5/9

print(convertir_a_celsius(98.6))  # 37.0
