from datetime import datetime, timedelta

def calcula_vencimiento_y_monto(numero_registro, numero_letra, fecha, aceptacion_plazo, monto, num_pagos):
    """Calcula la fecha de vencimiento y el monto a pagar de una letra.

    Args:
        numero_registro: El número de registro de la letra.
        numero_letra: El número de la letra.
        fecha: La fecha de emisión de la letra.
        aceptacion_plazo: El plazo de aceptación de la letra en días.
        monto: El monto de la letra.
        num_pagos: La cantidad de pagos que se realizarán.

    Returns:
        Una tupla con dos elementos: la fecha de vencimiento de la letra y el monto a pagar.
    """
    # Primero convertimos la fecha de emisión de la letra a un objeto datetime
    fecha_emision = datetime.strptime(fecha, '%Y-%m-%d')
    # Calculamos la fecha de vencimiento y el monto a pagar
    vencimiento = fecha_emision + timedelta(days=aceptacion_plazo)
    monto_a_pagar = monto + (monto * 0.03)
    # Devolvemos la fecha de vencimiento y el monto a pagar
    return (vencimiento, monto_a_pagar)

# Solicitamos los datos al usuario
numero_registro = input("Ingrese el número de registro de la letra: ")
numero_letra = input("Ingrese el número de la letra: ")
fecha = input("Ingrese la fecha de emisión de la letra (formato YYYY-MM-DD): ")
aceptacion_plazo = int(input("Ingrese el plazo de aceptación de la letra (en días): "))
monto = float(input("Ingrese el monto de la letra: "))
num_pagos = int(input("Ingrese la cantidad de pagos que se realizaran: "))

# Calculamos la fecha de vencimiento y el monto a pagar
vencimiento, monto_a_pagar = calcula_vencimiento_y_monto(numero_registro, numero_letra, fecha, aceptacion_plazo, monto, num_pagos)

# Calculamos las fechas y montos de los pagos
pagos = []
monto_pago = monto_a_pagar / num_pagos
fecha_pago = vencimiento
for i in range(num_pagos):
    pagos.append((fecha_pago, monto_pago))
    fecha_pago += timedelta(days=30)

# Imprimimos la fecha y el monto de cada pago
for pago in pagos:
    print(f'Fecha de pago: {pago[0].strftime("%d de %B de %Y")}, monto a pagar: {pago[1]}')

#compila