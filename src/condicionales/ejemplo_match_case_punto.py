punto = (0, 0)
# Los patrones pueden extraer valores de la tupla
match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        # Captura cualquier punto donde x=0, asigna y a la variable y
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        # Captura cualquier punto donde y=0
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        # Cualquier otro punto (x, y)
        print(f"El punto está en coordenadas x={x}, y={y}.")