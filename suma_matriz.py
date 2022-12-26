def sumar_matrices():
# elementos de la matriz B de 2 x 3 {[1.1][1.2][1.3]}
#                                   {[2.1][2.2][2.3]}

# elementos de la matriz B de 2 x 3 {[1.1][1.2][1.3]}
#                                   {[2.1][2.2][2.3]}

# Pedimos la producción de cada una de las máquinas del grupo A
  A = []
  print("Introduce la producción de cada una de las máquinas del grupo A:")
  for i in range(2):
    fila = []
    for j in range(3):
      fila.append(int(input(f"Introduce la producción de la máquina {i+1},{j+1}: ")))
    A.append(fila)

  # Pedimos la producción de cada una de las máquinas del grupo B
  B = []
  print("Introduce la producción de cada una de las máquinas del grupo B:")
  for i in range(2):
    fila = []
    for j in range(3):
      fila.append(int(input(f"Introduce la producción de la máquina {i+1},{j+1}: ")))
    B.append(fila)

  # Creamos una matriz resultado con las mismas dimensiones que A y B
  resultado = [[0 for j in range(len(A[0]))] for i in range(len(A))]

  # Recorremos cada elemento de las matrices A y B y lo sumamos
  for i in range(len(A)):
    for j in range(len(A[0])):
      resultado[i][j] = A[i][j] + B[i][j]

  return resultado

# Ejemplo de uso
resultado = sumar_matrices()
print(resultado)