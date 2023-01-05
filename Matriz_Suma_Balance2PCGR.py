# Pide al usuario que ingrese el número de filas y columnas de las matrices A y B
num_rows = int(input("Ingrese el número de filas de las matrices A y B: "))
num_cols = int(input("Ingrese el número de columnas de las matrices A y B: "))

# Define las matrices A y B como listas vacías
A = []
B = []

# Recorre las filas de ambas matrices y pide al usuario que ingrese los valores de cada fila
for i in range(num_rows):
  row_a = []
  row_b = []
  for j in range(num_cols):
    # Pide al usuario que ingrese el valor de la columna j de la fila i de A
    value_a = input(f"Ingrese el valor de la columna {j+1} de la fila {i+1} de la matriz A: ")
    row_a.append(value_a)
    # Pide al usuario que ingrese el valor de la columna j de la fila i de B
    value_b = input(f"Ingrese el valor de la columna {j+1} de la fila {i+1} de la matriz B: ")
    row_b.append(value_b)
  A.append(row_a)
  B.append(row_b)

# Define la matriz C como una lista vacía
C = []

# Recorre las filas de ambas matrices y realiza la suma de acuerdo a la condición descrita
for i in range(num_rows):
  row = []
  if A[i][0] == B[i][0]:
    # Si los valores de la columna 1 son iguales, agrega el valor de la columna 1 de A a la fila resultante
    row.append(A[i][0])
    # Suma los valores de la columna 2 de A y B
    row.append(int(A[i][1]) + int(B[i][1]))
  else:

    # Si los valores de la columna 1 no son iguales, concatena los valores de la columna 1 de A y B
    row.append(A[i][0] + B[i][0])
    # Agrega los valores de la columna 2 de A y B sin sumarlos
    row.append(A[i][1])
    row.append(B[i][1])
  C.append(row)
# Imprime el resultado
print(C)
# compila
