# Creamos un diccionario para almacenar la información de las operaciones
operaciones = {}

# Pedimos al usuario que ingrese el monto de apertura de cuenta
monto_apertura = float(input("Ingrese el monto de apertura de cuenta: "))

# Inicializamos la variable que llevará el registro del saldo actual
saldo_actual = monto_apertura

# Pedimos al usuario que ingrese la cantidad de operaciones a realizar
num_operaciones = int(input("Ingrese la cantidad de operaciones a realizar: "))

# Utilizamos un bucle while para iterar tantas veces como operaciones se hayan especificado
i = 0
while i < num_operaciones:
  # Preguntamos al usuario si desea realizar una operación de debe o de haber
  tipo_operacion = input("¿Desea realizar una operación de debe (D) o de haber (H)?: ")

  # Si el usuario elige una operación de debe, disminuimos el saldo actual y agregamos la información a nuestro diccionario
  if tipo_operacion == "D":
    monto = float(input("Ingrese el monto de la operación: "))
    saldo_actual -= monto
    operaciones[i] = {'tipo': 'debe', 'monto': monto}
  # Si el usuario elige una operación de haber, aumentamos el saldo actual y agregamos la información a nuestro diccionario
  elif tipo_operacion == "H":
    monto = float(input("Ingrese el monto de la operación: "))
    saldo_actual += monto
    operaciones[i] = {'tipo': 'haber', 'monto': monto}

  # Aumentamos la variable contadora del bucle
  i += 1

# Mostramos al usuario el saldo para el próximo mes
print("El saldo para el próximo mes es:", saldo_actual)
