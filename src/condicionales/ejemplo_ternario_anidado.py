edad = 20
# Ternario anidado (dentro del else)
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)