edad = 30
estado_civil = 'soltero'
if edad >= 18:
    # Solo si es mayor de edad, se evalúa el estado civil
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    # Si es menor de edad, no se pregunta por el estado civil
    print('Eres menor de edad.')