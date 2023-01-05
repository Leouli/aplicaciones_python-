#R_compras.py
def ingresar_compra():
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio unitario: "))
    igv = float(input("Ingrese el porcentaje de IGV: ")) / 100

    valor_venta = cantidad * precio
    impuesto_total = valor_venta * igv
    total = valor_venta + impuesto_total

    compra = {
        'producto': producto,
        'cantidad': cantidad,
        'precio': precio,
        'igv': igv,
        'valor_venta': valor_venta,
        'impuesto_total': impuesto_total,
        'total': total
    }

    compras.append(compra)


def mostrar_compras(compras):
    for compra in compras:
        print("Producto:", compra['producto'])
        print("Cantidad:", compra['cantidad'])
        print("Precio:", compra['precio'])
        print("IGV:", compra['igv'])
        print("Valor de venta:", compra['valor_venta'])
        print("Impuesto total:", compra['impuesto_total'])
        print("Total:", compra['total'])


compras = []

while True:
    opcion = input("¿Desea ingresar una compra? (s/n): ")
    if opcion.lower() == 's':
        ingresar_compra()
    else:
        break

mostrar_compras(compras)
