fruta = input("Introduzca una fruta: ")
# match-case compara el valor de fruta con cada patrón literal
match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        # El comodín _ coincide con cualquier valor no capturado antes
        print("Fruta desconocida.")