from datetime import datetime, timedelta


def obtener_datos():
    inicio_contrato = input("Ingrese la fecha de inicio de contrato (dd/mm/aaaa): ")
    categoria_muebles = input("Ingrese la categoría de muebles (A para altos o B para bajos): ")
    pago_mensual = input("Ingrese la monto del pago mensual: ")
    meses_alquiler = input("Ingrese la cantidad de meses que alquila el stand: ")
    num_stand = input("Ingrese el número de stand que alquila: ")
    nombre_propietario = input("Ingrese el nombre del propietario: ")
    giro_muebles = input("Ingrese el giro de los muebles: ")
    articulos_vende = input("Ingrese los artículos que vende: ")
    num_vendedoras = input("Ingrese el número de vendedoras que tiene en el stand: ")
    nombre_vendedora = input("Ingrese el nombre de la vendedora: ")
    num_discos = input("Ingrese el número de discos que tiene en el stand: ")
    return inicio_contrato, categoria_muebles, pago_mensual, meses_alquiler, num_stand, nombre_propietario, giro_muebles, articulos_vende, num_vendedoras, nombre_vendedora, num_discos


def calcular_fechas(inicio_contrato, meses_alquiler):
    # Convertimos la fecha de inicio de contrato a un objeto datetime
    inicio_contrato = datetime.strptime(inicio_contrato, "%d/%m/%Y")

    # Calculamos la fecha de pago sumando el número de meses de alquiler al objeto datetime de la fecha de inicio de contrato
    fecha_pago = inicio_contrato + timedelta(days=int(meses_alquiler) * 30)

    # Calculamos la fecha de cierre sumando 10 días a la fecha de p


def calcular_fechas(inicio_contrato, meses_alquiler):
    # Convertimos la fecha de inicio de contrato a un objeto datetime
    inicio_contrato = datetime.strptime(inicio_contrato, "%d/%m/%Y")

    # Calculamos la fecha de pago sumando el número de meses de alquiler al objeto datetime de la fecha de inicio de contrato
    fecha_pago = inicio_contrato + timedelta(days=int(meses_alquiler) * 30)

    # Calculamos la fecha de cierre sumando 10 días a la fecha de pago
    fecha_cierre = fecha_pago + timedelta(days=10)

    return fecha_pago, fecha_cierre


def calcular_interes(pago_mensual, dias_retraso):
    interes = float(pago_mensual) * (2/100) * dias_retraso
    return interes


def main():
    # Obtenemos los datos del usuario
    inicio_contrato, categoria_muebles, pago_mensual, meses


