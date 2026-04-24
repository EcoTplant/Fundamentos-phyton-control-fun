# Retornar múltiples valores (como tupla)
def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)  # Desempaquetado
print(f"Suma: {suma}, Promedio: {media}, Mínimo: {menor}, Máximo: {mayor}")
