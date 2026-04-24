numeros = [1, 2, 3, 4]
# Patrones de lista: se comprueba la longitud y se extraen elementos
match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        # El operador * captura el resto de elementos en una lista
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")