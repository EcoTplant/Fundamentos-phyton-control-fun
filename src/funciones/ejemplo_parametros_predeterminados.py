# Parámetros con valores por defecto
def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")           # Usa mensaje predeterminado: "¡Bienvenido!"
saludar("María", "¿Cómo estás hoy?")  # Usa mensaje personalizado
