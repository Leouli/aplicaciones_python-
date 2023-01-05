
# Creamos un diccionario para almacenar la información de las operaciones de debe
operaciones_debe = {'Deposito': 0, 'Transferencia recibida': 0, 'Notas de abono': 0, 'Letras en cobranza': 0}

# Creamos un diccionario para almacenar la información de las operaciones de haber
operaciones_haber = {'Giro de cheque': 0, 'Transferencia remitida': 0, 'Notas de cargo': 0, 'Comisiones bancarias': 0}

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

    # Si el usuario elige una operación de debe, le preguntamos qué tipo de operación desea realizar
    if tipo_operacion == "D":
        tipo_debe = input("¿Qué tipo de operación de debe desea realizar (Deposito, Transferencia recibida, Notas de abono, Letras en cobranza)?: ")
        monto = float(input("Ingrese el monto de la operación: "))

        saldo_actual += monto
        operaciones_debe[tipo_debe] += monto
    # Si el usuario elige una operación de haber, le preguntamos qué tipo de operación desea realizar
    elif tipo_operacion == "H":
        tipo_haber = input("¿Qué tipo de operación de haber desea realizar (Giro de cheque, Transferencia remitida, Notas de cargo, Comisiones bancarias)?: ")
        monto = float(input("Ingrese el monto de la operación: "))
        saldo_actual -= monto
        operaciones_haber[tipo_haber] += monto

  # Aumentamos la variable contadora del bucle
    i += 1

# Mostramos al usuario los totales de cada tipo de operación de debe
print("Totales de operaciones de debe:")
for tipo, total in operaciones_debe.items():
  print(f"{tipo}: {total}")

# Mostramos al usuario los totales de cada tipo de operación de haber
print("Totales de operaciones de haber:")
for tipo, total in operaciones_haber.items():
  print(f"{tipo}: {total}")

# Mostramos al usuario el saldo para el próximo mes
print("El saldo para el próximo mes es:", saldo_actual)


#si compila pero revisar