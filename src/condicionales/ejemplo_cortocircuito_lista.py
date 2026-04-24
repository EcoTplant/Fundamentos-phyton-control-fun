lista = []
# El operador and usa cortocircuito: si lista es False (vacía), no evalúa lista[0]
if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")
# Como lista está vacía, la condición es falsa y no se produce IndexError