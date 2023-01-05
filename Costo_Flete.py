# Costo_Flete.py
# Importamos la biblioteca numpy para trabajar con matrices
import numpy as np

# Definimos la lista de pesos de los paquetes
pesos = [10, 20, 30, 40, 50]

# Definimos el precio por kilogramo de transporte
precio_kg = 0.5

# Convertimos la lista de pesos en una matriz
matriz_pesos = np.array(pesos).reshape(5, 1)

# Creamos una matriz de unos con la misma cantidad de filas que la matriz de pesos
matriz_unos = np.ones((matriz_pesos.shape[0], 1))

# Multiplicamos la matriz de unos por el precio por kilogramo para obtener una matriz de precios
matriz_precios = matriz_unos * precio_kg

# Realizamos la multiplicación de matrices
matriz_resultado = np.dot(matriz_pesos, matriz_precios)

# Sumamos los valores de la matriz para obtener el costo total de transporte
costo_total = matriz_resultado.sum()

# Imprimimos el costo total de transporte
print(f"El costo total de transporte es ${costo_total}")

#no compila