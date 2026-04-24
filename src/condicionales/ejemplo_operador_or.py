dia = "sábado"
# El operador or necesita al menos una condición verdadera
if dia == "sábado" or dia == "domingo":
    # Cortocircuito: si la primera es verdadera, no evalúa la segunda
    print("Es fin de semana.")