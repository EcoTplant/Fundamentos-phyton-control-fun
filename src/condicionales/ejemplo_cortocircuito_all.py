condiciones = [True, True, False, True]
# all() devuelve False en cuanto encuentra un elemento falso (cortocircuito)
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")
# Se detiene en el False, no evalúa el último True