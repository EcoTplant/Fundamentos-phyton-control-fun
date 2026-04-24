edad = 25
ingresos = 30000
# El operador and exige que ambas condiciones sean verdaderas
if edad >= 18 and ingresos >= 20000:
    # Cortocircuito: si la primera es falsa, no evalúa la segunda
    print("Eres elegible para el crédito.")