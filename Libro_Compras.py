# Libro_Compras.py
# Se importa la librería math para usar la función round()
##import math


# Se define una función que calcula el valor de compra a partir de los datos de un registro
def calcular_valor_compra(importe_bruto, fletes, seguros, intereses, descuentos):
    valor_compra = importe_bruto + fletes + seguros + intereses - descuentos
    return valor_compra


# Se define una función que calcula el IGV a partir del valor de compra
def calcular_igv(valor_compra):
    igv = valor_compra * 0.18
    return igv


# Se define una función que calcula el precio de compra a partir del valor de compra y el IGV
def calcular_precio_compra(valor_compra, igv):
    precio_compra = valor_compra + igv
    return precio_compra


# Se pide al usuario que ingrese el número de registros a realizar
num_registros = int(input("Ingrese el número de registros a realizar: "))

# Se inicializan las variables que almacenarán los totales
total_importe_bruto = 0
total_fletes = 0
total_seguros = 0
total_intereses = 0
total_descuentos = 0
total_valor_compra = 0
total_igv = 0
total_precio_compra = 0

# Se itera sobre el número de registros a realizar
for i in range(num_registros):
    # Se pide al usuario que ingrese los datos de cada registro
    importe_bruto = float(input("Ingrese el importe bruto del registro {}: ".format(i + 1)))
    fletes = float(input("Ingrese los fletes del registro {}: ".format(i + 1)))
    seguros = float(input("Ingrese los seguros del registro {}: ".format(i + 1)))
    intereses = float(input("Ingrese los intereses del registro {}: ".format(i + 1)))
    descuentos = float(input("Ingrese los descuentos del registro {}: ".format(i + 1)))

    # Se calculan el valor de compra, el IGV y el precio de compra para el registro actual
    valor_compra = calcular_valor_compra(importe_bruto, fletes, seguros, intereses, descuentos)
    igv = calcular_igv(valor_compra)
    precio_compra = calcular_precio_compra(valor_compra, igv)

    # Se muestra al usuario la información ingresada y los totales del cálculo para el registro actual
print("Importe bruto: {}".format(importe_bruto))
print("Fletes: {}".format(fletes))
print("Seguros: {}".format(seguros))
print("Intereses: {}".format(intereses))
print("Descuentos: {}".format(descuentos))
print("Valor de compra: {}".format(valor_compra))
print("IGV: {}".format(igv))
print("Precio de compra: {}".format(precio_compra))

# Se actualizan los totales
total_importe_bruto += importe_bruto
total_fletes += fletes
total_seguros += seguros
total_intereses += intereses
total_descuentos += descuentos
total_valor_compra += valor_compra
total_igv += igv
total_precio_compra += precio_compra

# Una vez se han procesado todos los registros, se muestran los totales al usuario
print("Total importe bruto: {}".format(total_importe_bruto))
print("Total fletes: {}".format(total_fletes))
print("Total seguros: {}".format(total_seguros))
print("Total intereses: {}".format(total_intereses))
print("Total descuentos: {}".format(total_descuentos))
print("Total valor de compra: {}".format(total_valor_compra))
print("Total IGV: {}".format(total_igv))
print("Total precio de compra: {}".format(total_precio_compra))

#compila