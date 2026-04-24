a = True
b = False
c = not b  # c es True porque not False = True
# Precedencia: not > and > or. Por tanto, b and c se evalúa primero
resultado = a or b and c  # equivale a a or (b and c)
# b and c es False (b=False), luego True or False = True
print(resultado)  # Imprime True