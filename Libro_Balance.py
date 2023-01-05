# Importamos la librería de las partidas del plan contable
import plan_contable
import plan_contable
# Creamos las dos matrices vacías
matriz_balance = []
matriz_estado_resultados = []

# Pedimos al usuario que ingrese los datos de la matriz del balance
print("Ingrese los datos de la matriz del balance:")

# Iteramos hasta que el usuario ingrese una línea vacía
while True:
  partida = input("Ingrese la partida: ")
  if partida == "":
    break

  # Separamos la línea por el caracter ',' y convertimos a números
  # los montos (asumiendo que son números decimales)
  monto = input("Ingrese el monto: ")
  monto = float(monto)

  # Añadimos la línea a la matriz del balance
  matriz_balance.append((partida, monto))

# Pedimos al usuario que ingrese los datos de la matriz del estado de resultados
print("Ingrese los datos de la matriz del estado de resultados:")

# Iteramos hasta que el usuario ingrese una línea vacía
while True:
  linea = input()
  if linea == "":
    break

  # Separamos la línea por el caracter ',' y convertimos a números
  # los montos (asumiendo que son números decimales)
  partida, monto = linea.split(",")
  monto = float(monto)

  # Añadimos la línea a la matriz del estado de resultados
  matriz_estado_resultados.append((partida, monto))

# Creamos un diccionario con las sumas de cada partida del plan contable
suma_partidas = {}

# Recorremos las dos matrices y vamos sumando los montos de cada partida
for partida, monto in matriz_balance + matriz_estado_resultados:
  if partida in suma_partidas:
    suma_partidas[partida] += monto
  else:
    suma_partidas[partida] = monto

# Mostramos el resultado
for partida, monto in suma_partidas.items():
  print(f"{partida}: {monto}")
