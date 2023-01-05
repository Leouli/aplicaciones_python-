# Crea un diccionario para almacenar las partidas de cuentas y sus valores
partidas = {
    '10 CAJA Y BANCOS': [100, 200],
    '11 INVERSIONES FINANCIERAS': [300, 400],
    '12 CUENTAS POR COBRAR COMERCIALES – TERCEROS': [100, 200],
    '13 CUENTAS POR COBRAR COMERCIALES – RELACIONADAS': [100, 200],
    '14 CUENTAS POR COBRAR AL PERSONAL, A LOS ACCIONISTAS (SOCIOS), DIRECTORES Y GERENTES': [100, 200],
    '16 CUENTAS POR COBRAR DIVERSAS – TERCEROS': [100, 200],
    '17 CUENTAS POR COBRAR DIVERSAS – RELACIONADAS': [100, 200],
    '18 SERVICIOS Y OTROS CONTRATADOS POR ANTICIPADO': [100, 200],
    '19 ESTIMACIÓN DE CUENTAS DE COBRANZA DUDOSA': [100, 200],
    '20 MERCADERÍAS': [100, 200],
    '21 PRODUCTOS TERMINADOS': [100, 200],
    '22 SUBPRODUCTOS, DESECHOS Y DESPERDICIOS': [100, 200],
    '23 PRODUCTOS EN PROCESO': [100, 200],
    '24 MATERIAS PRIMAS': [100, 200],
    '25 MATERIALES AUXILIARES, SUMINISTROS Y REPUESTOS': [100, 200],
    '26 ENVASES Y EMBALAJES': [100, 200],
    '27 ACTIVOS NO CORRIENTES MANTENIDOS PARA LA VENTA': [100, 200],
    '28 EXISTENCIAS POR RECIBIR': [100, 200],
    '29 DESVALORIZACIÓN DE EXISTENCIAS': [100, 200],
    '30 INVERSIONES MOBILIARIAS': [100, 200],
    '31 INVERSIONES INMOBILIARIAS': [100, 200],
    '32 ACTIVOS ADQUIRIDOS EN ARRENDAMIENTO FINANCIERO': [100, 200],
    '33 INMUEBLES, MAQUINARIA Y EQUIPO': [100, 200],
    '34 INTANGIBLES': [100, 200],
    '35 ACTIVOS BIOLÓGICOS': [100, 200],
    '36 DESVALORIZACIÓN DE ACTIVO INMOVILIZADO': [100, 200],
    '37 ACTIVO DIFERIDO': [100, 200],
    '38 OTROS ACTIVOS': [100, 200],
    '39 DEPRECIACIÓN, AMORTIZACIÓN Y AGOTAMIENTO ACUMULADOS': [100, 200],
    '40 TRIBUTOS, CONTRAPRESTACIONES Y APORTES AL SISTEMA DE PENSIONES Y DE': [100, 200],
    '41 REMUNERACIONES Y PARTICIPACIONES POR PAGAR': [100, 200],
    '42 CUENTAS POR PAGAR COMERCIALES – TERCEROS': [100, 200],
    '43 CUENTAS POR PAGAR COMERCIALES – RELACIONADAS': [100, 200],
    '44 CUENTAS POR PAGAR A LOS ACCIONISTAS (SOCIOS), DIRECTORES Y GERENTES': [100, 200],
    '46 CUENTAS POR PAGAR DIVERSAS – TERCEROS': [100, 200],
    '47 CUENTAS POR PAGAR DIVERSAS – RELACIONADAS': [100, 200],
    '48 PROVISIONES': [100, 200],
    '49 PASIVO DIFERIDO': [100, 200],
    '50 CAPITAL': [100, 200],
    '52 CAPITAL ADICIONAL': [100, 200],
    '56 RESULTADOS NO REALIZADOS': [100, 200],
    '57 EXCEDENTE DE REVALUACIÓN': [100, 200],
    '58 RESERVAS': [100, 200],
    '59 RESULTADOS ACUMULADOS': [100, 200],
    '60 COMPRAS': [100, 200],
    '61 VARIACIÓN DE EXISTENCIAS': [100, 200],
    '62 GASTOS DE PERSONAL, DIRECTORES Y GERENTES': [100, 200],
    '63 GASTOS DE SERVICIOS PRESTADOS POR TERCEROS': [100, 200],
    '64 GASTOS POR TRIBUTOS': [100, 200],
    '65 OTROS GASTOS DE GESTION': [100, 200],
    '66 PERDIDA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE': [100, 200],
    '67 GASTOS FINANCIEROS': [100, 200],
    '68 VALUACIÓN Y DETERIORO DE ACTIVOS Y PROVISIONES': [100, 200],
    '69 COSTO DE VENTAS': [100, 200],
    '70 VENTAS': [100, 200],
    '71 VARIACIÓN DE LA PRODUCCIÓN ALMACENADA': [100, 200],
    '72 PRODUCCIÓN DE ACTIVO INMOVILIZADO': [100, 200],
    '73 DESCUENTOS, REBAJAS Y BONIFICACIONES OBTENIDOS': [100, 200],
    '74 DESCUENTOS, REBAJAS Y BONIFICACIONES CONCEDIDOS': [100, 200],
    '75 OTROS INGRESOS DE GESTIÓN': [100, 200],
    '76 GANANCIA POR MEDICIÓN DE ACTIVOS NO FINANCIEROS AL VALOR RAZONABLE': [100, 200],
    '77 INGRESOS FINANCIEROS': [100, 200],
    '78 CARGAS CUBIERTAS POR PROVISIONES': [100, 200],
    '79 CARGAS IMPUTABLES A CUENTAS DE COSTOS Y GASTOS': [100, 200],
    '80 MARGEN COMERCIAL': [100, 200],
    '81 PRODUCCIÓN DEL EJERCICIO': [100, 200],
    '82 VALOR AGREGADO': [100, 200],
    '83 EXCEDENTE BRUTO (INSUFICIENCIA BRUTA) DE EXPLOTACIÓN': [100, 200],
    '84 RESULTADO DE EXPLOTACIÓN': [100, 200],
    '85 RESULTADO ANTES DE PARTICIPACIONES E IMPUESTOS': [100, 200],
    '87 PARTICIPACIONES DE LOS TRABAJADORES': [100, 200],
    '88 IMPUESTO A LA RENTA': [100, 200],
    '89 DETERMINACIÓN DEL RESULTADO DEL EJERCICIO': [100, 200],

}

# Crea las matrices A y B utilizando los valores del diccionario
partidas = {}
A = [[key] + value for key, value in partidas.items()]
B = [[key] + value for key, value in partidas.items()]

# Calcula la diferencia entre las matrices A y B
filas = len(A)
columnas = len(A[0])
C = []

for i in range(filas):
    fila = [A[i][0]]
    for j in range(1, columnas):
        fila.append(A[i][j] - B[i][j])
    C.append(fila)

print(C)

# Obtén el número de filas y columnas de las matrices
M = int(input("Ingrese el número de filas de las matrices A y B: "))
N = int(input("Ingrese el número de columnas de las matrices A y B: "))

# Crea las matrices vacías
A = [['' for j in range(N)] for i in range(M)]
B = [['' for j in range(N)] for i in range(M)]
C = [['' for j in range(N)] for i in range(M)]

# Pide al usuario que ingrese los valores de la matriz A
print("Ingrese los valores de la matriz A:")
for i in range(M):
  for j in range(N):
    A[i][j] = input("Ingrese el elemento A[{}][{}]: ".format(i+1, j+1))

# Pide al usuario que ingrese los valores de la matriz B
print("Ingrese los valores de la matriz B:")
for i in range(M):
  for j in range(N):
    B[i][j] = input("Ingrese el elemento B[{}][{}]: ".format(i+1, j+1))

# Realiza la diferencia entre las matrices y guarda el resultado en la matriz C
for i in range(M):
  for j in range(N):
    # Verifica si los elementos de A y B son números antes de restarlos
    if A[i][j].isnumeric() and B[i][j].isnumeric():
      C[i][j] = int(A[i][j]) - int(B[i][j])
    else:
      C[i][j] = ''

# Imprime el resultado final
print("Resultado:")
for fila in C:
  print(fila)



