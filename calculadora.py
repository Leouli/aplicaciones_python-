#calculadora.py
def sumar(a, b):
  return a + b

def restar(a, b):
  return a - b

def multiplicar(a, b):
  return a * b

def dividir(a, b):
  return a / b

operacion = input("¿Qué operación deseas realizar? (sumar / restar / multiplicar / dividir): ")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if operacion == "sumar":
  resultado = sumar(a, b)
elif operacion == "restar":
  resultado = restar(a, b)
elif operacion == "multiplicar":
  resultado = multiplicar(a, b)
elif operacion == "dividir":
  resultado = dividir(a, b)
else:
  print("Operación inválida.")

print("El resultado es:", resultado)
#compila