def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"

# Diferentes formas de llamar
print(calcular_pago(40))            # 40 horas, tarifa predeterminada
print(calcular_pago(35, 20))        # 35 horas, tarifa 20
print(calcular_pago(30, moneda="USD"))  # moneda especificada por nombre
print(calcular_pago(horas=25, tarifa=18, moneda="GBP"))  # todo por nombre
