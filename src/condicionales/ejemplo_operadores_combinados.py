edad = 17
permiso_parental = True
# Combinación de and y or. Los paréntesis mejoran la legibilidad
if (edad >= 18) or (edad >= 16 and permiso_parental):
    # Se cumple si: (mayor de edad) o (al menos 16 y con permiso)
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")