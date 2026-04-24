saldo = 300
retiro = 500
if saldo >= retiro:
    # Si hay fondos suficientes, se actualiza el saldo y se muestra el nuevo saldo
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    # Si no hay fondos, se informa y se muestra el saldo actual
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")