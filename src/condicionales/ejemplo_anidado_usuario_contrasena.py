usuario = 'admin'
contrasena = '1234'
# Verificación por pasos: primero usuario, luego contraseña
if usuario == 'admin':
    # Solo si el usuario es correcto, se comprueba la contraseña
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')