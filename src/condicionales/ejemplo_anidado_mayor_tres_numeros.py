a = 5
b = 10
c = 15
# Algoritmo anidado para hallar el mayor de tres números (no recomendado por complejidad)
if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')