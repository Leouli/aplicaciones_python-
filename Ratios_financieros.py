#Ratios_financieros.py
def ingresar_estados_financieros():
    activo_total = float(input("Ingrese el activo total: "))
    pasivo_total = float(input("Ingrese el pasivo total: "))
    patrimonio_neto = float(input("Ingrese el patrimonio neto: "))
    total_ingresos = float(input("Ingrese el total de ingresos: "))
    total_costos = float(input("Ingrese el total de costos: "))
    total_gastos = float(input("Ingrese el total de gastos: "))

    return (activo_total, pasivo_total, patrimonio_neto, total_ingresos, total_costos, total_gastos)


def calcular_ratios(activo_total, pasivo_total, patrimonio_neto, total_ingresos, total_costos, total_gastos):
    ratio_liquidez = activo_total / pasivo_total
    ratio_endeudamiento = pasivo_total / patrimonio_neto
    ratio_rentabilidad = total_ingresos / total_costos
    ratio_rentabilidad_sobre_patrimonio_neto = (total_ingresos - total_gastos) / patrimonio_neto

    return (ratio_liquidez, ratio_endeudamiento, ratio_rentabilidad, ratio_rentabilidad_sobre_patrimonio_neto)


def mostrar_ratios(ratios):
    print("Ratio de liquidez:", ratios[0])
    print("Ratio de endeudamiento:", ratios[1])
    print("Ratio de rentabilidad:", ratios[2])
    print("Ratio de rentabilidad sobre el patrimonio neto:", ratios[3])


estados_financieros = ingresar_estados_financieros()
ratios = calcular_ratios(*estados_financieros)
mostrar_ratios(ratios)
