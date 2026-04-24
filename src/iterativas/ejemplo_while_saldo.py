saldo = 1000
while saldo > 0:
    print(f"Saldo actual: {saldo}€")
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))
    if gasto == 0:
        break  # Sale del bucle inmediatamente
    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue  # Vuelve al inicio del bucle
    saldo -= gasto
print(f"Saldo final: {saldo}€")
