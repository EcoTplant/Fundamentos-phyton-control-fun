def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []
    for campo in campos_requeridos:
        if campo not in datos:
            errores.append(f"Falta el campo requerido: {campo}")
            break
        elif not datos[campo]:
            errores.append(f"El campo {campo} no puede estar vacío")
            break
    else:
        # Solo si todos los campos requeridos están presentes y no vacíos
        if "@" not in datos["email"]:
            errores.append("Email inválido")
        try:
            edad = int(datos["edad"])
            if edad < 18 or edad > 120:
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")
    if "telefono" in datos:
        if not datos["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Explícitamente indicamos que es opcional
    return {"valido": len(errores) == 0, "errores": errores}

formulario1 = {"nombre": "Ana García", "email": "ana@ejemplo.com", "edad": "28"}
formulario2 = {"nombre": "Carlos López", "email": "carlosejemplo.com", "edad": "17"}
print(validar_formulario(formulario1))
print(validar_formulario(formulario2))
