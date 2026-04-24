def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")
