#MCD.py
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

# Ejemplo de uso
mcd(12, 18)
# Devuelve 6



# Importamos el módulo `math`
import math

# Definimos los dos números para los que queremos calcular el MCM
num1 = 15
num2 = 20

# Calculamos el MCD de los dos números
mcd = math.gcd(num1, num2)

# Calculamos el MCM utilizando la fórmula mencionada anteriormente
mcm = (num1 * num2) / mcd

# Mostramos el resultado
print(mcm)  # Imprime: 60

