edad = 16
permiso_padres = True
if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    # Anidamiento dentro del else
    if edad >= 16:
        # Segundo nivel: verifica permiso de padres
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')