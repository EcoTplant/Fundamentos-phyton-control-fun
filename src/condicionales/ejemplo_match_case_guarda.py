edad = 20
# Las guardas (if después del patrón) permiten condiciones adicionales
match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")