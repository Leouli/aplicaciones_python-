# Libro_Ventas.py
# Importamos la librería de cálculo matemático
import math

# Pedimos al usuario que ingrese el número de registros a procesar
num_registros = int(input("Ingrese el número de registros a procesar: "))

# Creamos variables para almacenar los totales
total_importe_bruto = 0
total_fletes = 0
total_intereses = 0
total_descuentos = 0
total_valor_venta = 0
total_igv = 0
total_precio_venta = 0

# Iteramos por cada uno de los registros
for i in range(num_registros):
    # Pedimos al usuario que ingrese los datos para el cálculo
    importe_bruto = float(input("Ingrese el importe bruto para el registro {}: ".format(i + 1)))
    fletes = float(input("Ingrese los fletes para el registro {}: ".format(i + 1)))
    intereses = float(input("Ingrese los intereses para el registro {}: ".format(i + 1)))
    descuentos = float(input("Ingrese los descuentos para el registro {}: ".format(i + 1)))

    # Calculamos el valor de venta
    valor_venta = importe_bruto + fletes + intereses - descuentos

    # Calculamos el IGV (asumimos un IGV del 18%)
    igv = valor_venta * 0.18

    # Calculamos el precio de venta
    precio_venta = valor_venta + igv

    # Imprimimos los resultados para el registro actual
    print("Registro número {}".format(i + 1))
    print("Importe bruto: {}".format(importe_bruto))
    print("Fletes: {}".format(fletes))
    print("Intereses: {}".format(intereses))
    print("Descuentos: {}".format(descuentos))
    print("Valor de venta: {}".format(valor_venta))
    print("IGV: {}".format(igv))
    print("Precio de venta: {}".format(precio_venta))

    # Acumulamos los totales
    total_importe_bruto += importe_bruto
    total_fletes += fletes
    total_intereses += intereses
    total_descuentos += descuentos
    total_valor_venta += valor_venta
    total_igv += igv
    total_precio_venta += precio_venta

# Imprimimos los totales finales
print("Total importe bruto: {}".format(total_importe_bruto))
print("Total fletes: {}".format(total_fletes))
print("Total intereses: {}".format(total_intereses))
print("Total descuentos: {}".format(total_descuentos))
print("Total valor de venta: {}".format(total_valor_venta))
print("Total IGV: {}".format(total_igv))
print("Total precio de venta: {}".format(total_precio_venta))

#compila