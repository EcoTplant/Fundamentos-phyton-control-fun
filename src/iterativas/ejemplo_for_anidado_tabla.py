# Tabla de multiplicar 3x3 con bucles anidados
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i*j}", end="\t")
    print()  # Salta a la siguiente fila
