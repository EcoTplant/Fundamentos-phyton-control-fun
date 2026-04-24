numeros = [0, 0, 1, 0]
# any() devuelve True en cuanto encuentra un elemento verdadero (cortocircuito)
if any(numeros):
    print("Al menos un número es no cero.")
# La evaluación se detiene en el 1, sin revisar el último 0