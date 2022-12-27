#ubicacion.py
# Inicializar el arreglo vacío
arreglo = []

# Pedir el número de elementos del arreglo
num_elementos = int(input("Ingresa el número de elementos del arreglo: "))

# Pedir el ingreso de cada elemento del arreglo
for i in range(num_elementos):
  elemento = input(f"Ingresa el elemento {i+1}: ")
  arreglo.append(elemento)

# Pedir el elemento para buscar su ubicación
elemento_buscado = input("Ingresa el elemento que deseas buscar: ")

# Buscar la ubicación del elemento en el arreglo
try:
  ubicacion = arreglo.index(elemento_buscado)
  print(f"El elemento se encuentra en la posición {ubicacion} del arreglo.")
except ValueError:
  print("El elemento no se encuentra en el arreglo.")
