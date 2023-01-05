def sumar_matrices(A, B, M, N):
  resultado = [[0 for j in range(N)] for i in range(M)]
  for i in range(M):
    for j in range(N):
      resultado[i][j] = A[i][j] + B[i][j]
  return resultado

def restar_matrices(A, B, M, N):
  resultado = [[0 for j in range(N)] for i in range(M)]
  for i in range(M):
    for j in range(N):
      resultado[i][j] = A[i][j] - B[i][j]
  return resultado

def multiplicar_matrices(A, B, M, N, P):
  resultado = [[0 for j in range(P)] for i in range(M)]
  for i in range(M):
    for j in range(P):
      for k in range(N):
        resultado[i][j] += A[i][k] * B[k][j]
  return resultado

operacion = input("¿Qué operación deseas realizar? (sumar / restar / multiplicar): ")

M = int(input("Ingrese el número de filas de la matriz A: "))
N = int(input("Ingrese el número de columnas de la matriz A: "))
P = int(input("Ingrese el número de columnas de la matriz B: "))

A = [[0 for j in range(N)] for i in range(M)]
B = [[0 for j in range(P)] for i in range(N)]

print("Ingrese los valores de la matriz A:")
for i in range(M):
  for j in range(N):
    A[i][j] = int(input("Ingrese el elemento A[{}][{}]: ".format(i+1, j+1)))

print("Ingrese los valores de la matriz B:")
for i in range(N):
  for j in range(P):
    B[i][j] = int(input("Ingrese el elemento B[{}][{}]: ".format(i+1, j+1)))

if operacion == "sumar":
  resultado = sumar_matrices(A, B, M, N)
elif operacion == "restar":
  resultado = restar_matrices(A, B, M, N)
elif operacion == "multiplicar":
  resultado = multiplicar_matrices(A, B, M, N, P)
else:
  print("Operación inválida.")
print("Resultado:")
for fila in resultado:
  print(fila)

