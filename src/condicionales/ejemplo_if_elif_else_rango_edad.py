edad = 45
if edad < 18:
    # Menor de edad
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    # Comparación encadenada: edad entre 18 y 64 (ambos inclusive)
    print("Eres adulto.")
else:
    # Edad >= 65
    print("Eres mayor de 65 años.")