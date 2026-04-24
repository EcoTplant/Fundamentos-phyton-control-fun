numero = 0
if numero > 0:
    # Primera condición: número positivo
    print("El número es positivo.")
elif numero < 0:
    # Segunda condición: número negativo (solo se evalúa si la primera es falsa)
    print("El número es negativo.")
else:
    # Si ninguna condición anterior es verdadera, el número debe ser cero
    print("El número es cero.")