contrasena = input("Introduce la contraseña: ")
if contrasena == "secreta123":
    # Compara la cadena introducida con la esperada. Si es igual, acceso concedido.
    print("Acceso concedido.")
else:
    # Si no coincide, se deniega el acceso
    print("Contraseña incorrecta. Acceso denegado.")