# Buenas prácticas: verbos en presente, tipos, ejemplos
def generar_contraseña(longitud=8):
    """Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """
    import random, string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def contar_palabras(texto):
    """Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """
    return len(texto.split())

def formatear_nombre(nombre, apellido):
    """Formatea un nombre completo en formato 'Apellido, Nombre'.

    Ejemplo:
        >>> formatear_nombre("Juan", "Pérez")
        'Pérez, Juan'
    """
    return f"{apellido}, {nombre}"

def obtener_elemento(lista, indice):
    """Obtiene un elemento de una lista por su índice.

    Raises:
        IndexError: Si el índice está fuera del rango
    """
    return lista[indice]

print(contar_palabras("Hola mundo"))  # 2
print(formatear_nombre("Ana", "López"))  # López, Ana
