#Suma_matrices_MxN.py
# Obtén el número de filas y columnas de las matrices
M = int(input("Ingrese el número de filas de la matriz A: "))
N = int(input("Ingrese el número de columnas de la matriz A y la matriz B: "))

# Crea las matrices vacías
A = [[0 for j in range(N)] for i in range(M)]
B = [[0 for j in range(N)] for i in range(M)]
resultado = [[0 for j in range(N)] for i in range(M)]

# Pide al usuario que ingrese los valores de la matriz A
print("Ingrese los valores de la matriz A:")
for i in range(M):
  for j in range(N):
    A[i][j] = int(input("Ingrese el elemento A[{}][{}]: ".format(i+1, j+1)))

# Pide al usuario que ingrese los valores de la matriz B
print("Ingrese los valores de la matriz B:")
for i in range(M):
  for j in range(N):
    B[i][j] = int(input("Ingrese el elemento B[{}][{}]: ".format(i+1, j+1)))

# Realiza la suma de las matrices
for i in range(M):
  for j in range(N):
    resultado[i][j] = A[i][j] + B[i][j]

# Imprime el resultado final
print("Resultado:")
for fila in resultado:
  print(fila)

