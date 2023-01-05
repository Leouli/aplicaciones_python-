# Ganancia_ventas.py
# Importamos la biblioteca numpy para trabajar con matrices
import numpy as np

# Definimos la lista de frutas
frutas = ["Manzanas", "Peras", "Naranjas", "Uvas"]

# Definimos la lista de precios
precios = [1, 2, 3, 4]

# Definimos la lista de cantidades
cantidades = [10, 20, 30, 40]

# Convertimos las listas en matrices
matriz_frutas = np.array(frutas).reshape(4, 1)
matriz_precios = np.array(precios).reshape(1, 4)
matriz_cantidades = np.array(cantidades).reshape(4, 1)

# Realizamos la multiplicación de matrices
matriz_resultado = np.dot(matriz_cantidades, matriz_precios)

# Sumamos los valores de la matriz para obtener el total de dinero ganado
total_dinero = matriz_resultado.sum()

# Imprimimos el total de dinero ganado
print(f"Hemos ganado un total de ${total_dinero} en el último mes")

no compola