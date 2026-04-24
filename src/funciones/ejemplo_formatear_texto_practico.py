# Función práctica que combina varios tipos de parámetros
def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    if mayusculas:
        texto = texto.upper()
    palabras = texto.split()
    palabras_formateadas = [f"{prefijo}{palabra}{sufijo}" for palabra in palabras]
    resultado = separador.join(palabras_formateadas)
    return resultado

texto_original = "python es un lenguaje versátil"
print(formatear_texto(texto_original))
print(formatear_texto(texto_original, mayusculas=True))
print(formatear_texto(texto_original, prefijo="«", sufijo="»"))
print(formatear_texto(texto_original, separador="-"))
print(formatear_texto(texto_original, mayusculas=True, prefijo="#", sufijo="!", separador="..."))
