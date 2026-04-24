def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    return [num for num in lista if num % 2 == 0]

print(filtrar_pares([1,2,3,4,5,6]))  # [2,4,6]
