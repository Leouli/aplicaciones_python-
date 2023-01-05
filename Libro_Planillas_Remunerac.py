# Definición de variables
num_trabajador = 0
fecha_ingreso = ""
sueldo_base = 0
fecha_inicio_vacaciones = ""
fecha_fin_vacaciones = ""
descuentos_trabajador = 0
aportes_trabajador = 0
aportes_empleador = 0

# Tasas de descuento y aporte
tasa_snp = 0.1 # 10% de descuento para el SNP
tasa_afp = 0.2 # 20% de descuento para la AFP
tasa_5ta_categoria = 0.05 # 5% de descuento para la 5ta Categoría
tasa_ips = 0.03 # 3% de descuento para el IPS
tasa_bonificacion_costo_vida = 0.03 # 3% de aporte para bonificación por costo de vida
tasa_comisiones = 0.05 # 5% de aporte para comisiones
tasa_gratificaciones = 0.1 # 10% de aporte para gratificaciones
tasa_movilidad = 0.03 # 3% de aporte para movilidad
tasa_asignacion_familiar = 0.05 # 5% de aporte para asignación familiar

# Solicitud de datos al usuario
num_trabajador = int(input("Ingrese el número de trabajador: "))
fecha_ingreso = input("Ingrese la fecha de ingreso del trabajador: ")
sueldo_base = float(input("Ingrese el sueldo base del trabajador: "))
fecha_inicio_vacaciones = input("Ingrese la fecha de inicio de vacaciones del trabajador: ")
fecha_fin_vacaciones = input("Ingrese la fecha de fin de vacaciones del trabajador: ")

# Cálculo de descuentos del trabajador
tasa_snp = 0.1 # 10% de # Escritura de datos en archivo CSV
import csv
with open(nombre_archivo + ".csv", "w", newline="") as archivo:
  writer = csv.writer(archivo)
  writer.writerow(["Total de descuentos", "$" + str(total_descuentos)])
  writer.writerow(["Total de aportes del trabajador", "$" + str(total_aportes_trabajador)])
  writer.writerow(["Total de aportes del empleador", "$" + str(total_aportes_empleador)])
SNP
tasa_afp = 0.2 # 20% de
# ***********************************************************

# Importación de la librería datetime
import datetime

# Conversión de fechas a objetos datetime
fecha_inicio_vacaciones = datetime.datetime.strptime(fecha_inicio_vacaciones, "%d/%m/%Y")
fecha_fin_vacaciones = datetime.datetime.strptime(fecha_fin_vacaciones, "%d/%m/%Y")

# Cálculo de la duración de las vacaciones en días
duracion_vacaciones = fecha_fin_vacaciones - fecha_inicio_vacaciones
duracion_vacaciones_dias = duracion_vacaciones.days

# Cálculo de descuentos del trabajador
descuentos_snp = sueldo_base * tasa_snp * duracion_vacaciones_dias / 30
descuentos_afp = sueldo_base * tasa_afp * duracion_vacaciones_dias / 30
descuentos_5ta_categoria = sueldo_base * tasa_5ta_categoria * duracion_vacaciones_dias / 30
descuentos_ips = sueldo_base * tasa_ips * duracion_vacaciones_dias / 30
descuentos_trabajador = descuentos_snp + descuentos_afp + descuentos_5ta_categoria + descuentos_ips

# Cálculo de aportes del trabajador y del empleador
aportes_trabajador = sueldo_base *

# ***********************************************************

# Cálculo de aportes del trabajador y del empleador
aportes_bonificacion_costo_vida = sueldo_base * tasa_bonificacion_costo_vida * duracion_vacaciones_dias / 30
aportes_comisiones = sueldo_base * tasa_comisiones * duracion_vacaciones_dias / 30
aportes_gratificaciones = sueldo_base * tasa_gratificaciones * duracion_vacaciones_dias / 30
aportes_movilidad = sueldo_base * tasa_movilidad * duracion_vacaciones_dias / 30
aportes_asignacion_familiar = sueldo_base * tasa_asignacion_familiar * duracion_vacaciones_dias / 30
aportes_trabajador = aportes_bonificacion_costo_vida + aportes_comisiones + aportes_gratificaciones + aportes_movilidad + aportes_asignacion_familiar
aportes_empleador = sueldo_base * tasa_aportes_empleador * duracion_vacaciones_dias / 30

# Cálculo del saldo final del trabajador
saldo_final = sueldo_base - descuentos_trabajador + aportes_trabajador + aportes_empleador

# Impresión de resultados
print("Sueldo base: $" + str(sueldo_base))
print("Descuentos del trabajador: $" + str(descuentos_trabajador))
print("Aportes del trabajador: $" + str(aportes_trabajador))
print("Aportes del empleador: $" + str(aportes_empleador))


# ***********************************************************

# Cálculo del monto total de descuentos, aportes del trabajador y aportes del empleador
monto_total_descuentos = descuentos_trabajador
monto_total_aportes_trabajador = aportes_trabajador
monto_total_aportes_empleador = aportes_empleador

# Impresi


# ***********************************************************

# Impresión de resumen de la planilla de remuneraciones
print("Número de trabajador: " + str(num_trabajador))
print("Fecha de ingreso: " + fecha_ingreso)
print("Sueldo base: $" + str(sueldo_base))
print("Saldo final: $" + str(saldo_final))
print("Monto total de descuentos: $" + str(monto_total_descuentos))
print("Monto total de aportes del trabajador: $" + str(monto_total_aportes_trabajador))
print("Monto total de aportes del empleador: $" + str(monto_total_aportes_empleador))

# Solicitud al usuario si desea generar un archivo de texto con la planilla de remuneraciones
generar_archivo = input("¿Desea generar un archivo de texto con la planilla de remuneraciones? (s/n) ")

if generar_archivo == "s":
  # Solicitud del nombre del archivo
  nombre_archivo = input("Ingrese el nombre del archivo: ")

  # Escritura de datos en archivo CSV
  import csv
  with open(nombre_archivo + ".csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Número de trabajador", "Fecha de ingreso",

# ***********************************************************

# Lectura de datos de archivo CSV
import csv

with open("datos_trabajadores.csv", "r") as archivo:
    reader = csv.reader(archivo)
datos_trabajadores = list(reader)

# Inicialización de variables
total_descuentos = 0
total_aportes_trabajador = 0
total_aportes_empleador = 0

# Recorrido de la lista de trabajadores y cálculo de montos
for trabajador in datos_trabajadores:
# Asignación de variables
    num_trabajador = trabajador[0]
fecha_ingreso = trabajador[1]
sueldo_base = float(trabajador[2])
fecha_inicio_vacaciones = trabajador[3]
fecha_fin_vacaciones = trabajador[4]

# Cálculo de descuentos, aportes del trabajador y aportes del empleador
# (la lógica para realizar estos cálculos puede ser similar a la utilizada en el ejemplo anterior)
descuentos_trabajador = ...
aportes_trabajador = ...
aportes_empleador = ...

# Cálculo de totales
total_descuentos += descuentos_trabajador
total_aportes_trabajador += aportes_trabaj

# ***********************************************************

# Impresión de resumen de planillas de remuneraciones
print("Total de descuentos: $" + str(total_descuentos))
print("Total de aportes del trabajador: $" + str(total_aportes_trabajador))
print("Total de aportes del empleador: $" + str(total_aportes_empleador))

# Solicitud al usuario si desea generar un archivo de texto con el resumen de planillas de remuneraciones
generar_archivo = input("¿Desea generar un archivo de texto con el resumen de planillas de remuneraciones? (s/n) ")

if generar_archivo == "s":
  # Solicitud del nombre del archivo
  nombre_archivo = input("Ingrese el nombre del archivo: ")

  # Escritura de datos en archivo CSV
  import csv
  with open(nombre_archivo + ".csv", "w", newline="

  # ***********************************************************

  # Escritura de datos en archivo CSV
  import csv
  with open(nombre_archivo + ".csv", "w", newline="") as archivo:
      writer = csv.writer(archivo)
writer.writerow(["Total de descuentos", "$" + str(total_descuentos)])
writer.writerow(["Total de aportes del trabajador", "$" + str(total_aportes_trabajador)])
writer.writerow(["Total de aportes del empleador", "$" + str(total_aportes_empleador)])

