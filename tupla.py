#tupla.py
# Crear una tupla con valores iniciales
numeros = (1, 2, 3, 4, 5)

# Usar un ciclo while para recorrer la tupla
i = 0
while i < len(numeros):
    numero = numeros[i]

    # Usar una estructura if para verificar una condición
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

    # Incrementar el contador para seguir recorriendo la tupla
    i += 1
