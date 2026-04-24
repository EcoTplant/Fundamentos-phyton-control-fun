# Coherencia en tipos de retorno: siempre devuelve lista
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error
    return [num for num in numeros if num > 0]

# Return temprano para casos especiales
def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"
    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"
    return "Insuficiente"

print(filtrar_positivos([-1, 2, -3, 4]))  # [2, 4]
print(obtener_calificacion(85))           # Notable
