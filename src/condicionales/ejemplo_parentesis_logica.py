a = True
b = False
c = True
# Los paréntesis fuerzan el orden de evaluación: primero (a or b)
resultado = (a or b) and c  # (True or False) = True, luego True and True = True
print(resultado)  # Imprime True