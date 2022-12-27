#multiplicacion_matrices.py
def multiplicar_matrices(M, L, N):
  # Crea la matriz A con 3 filas y 4 columnas
  A = [[float(input("Ingresa el elemento ({},{}) de la matriz A: ".format(i + 1, j + 1))) for j in range(4)] for i in
       range(3)]

  # Crea la matriz B con 4 filas y 5 columnas
  B = [[float(input("Ingresa el elemento ({},{}) de la matriz B: ".format(i + 1, j + 1))) for j in range(5)] for i in
       range(4)]
  # Crea una matriz resultante vacía con M filas y N columnas
  resultado = [[0 for j in range(N)] for i in range(M)]

  # Recorre las filas de la matriz resultante
  for i in range(M):
    # Recorre las columnas de la matriz resultante
    for j in range(N):
      # Inicializa el acumulador en 0
      acumulador = 0
      # Recorre las columnas de la matriz A y las filas de la matriz B
      for k in range(L):
        # Multiplica cada elemento de la fila de la matriz A por cada elemento de la columna de la matriz B y suma los resultados
        acumulador += A[i][k] * B[k][j]
      # Almacena el resultado en la matriz resultante
      resultado[i][j] = acumulador

  return resultado

# Solicita al usuario que ingrese los valores de M, L y N
M = int(input("Ingresa el valor de M: "))
L = int(input("Ingresa el valor de L: "))
N = int(input("Ingresa el valor de N: "))

# Crea las matrices A y B con los valores ingresados por el usuario
A = [[int(input("Ingresa el elemento ({},{}) de la matriz A: ".format(i+1, j+1))) for j in range(L)] for i in range(M)]
B = [[int(input("Ingresa el elemento ({},{}) de la matriz B: ".format(i+1, j+1))) for j in range(N)] for i in range(L)]

# Multiplica las matrices A y B y almacena el resultado en la matriz resultante
resultado = multiplicar_matrices(M, L, N)

# Imprime la matriz resultante
for fila in resultado:
  print(fila)
  # compila

