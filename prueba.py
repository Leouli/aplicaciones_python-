# Creamos un diccionario para almacenar la información de la mercancía
mercancia = {}

# Inicializamos la variable que llevará el registro del stock actual
stock_actual = 0

# Pedimos al usuario que ingrese la cantidad de operaciones a realizar
num_operaciones = int(input("Ingrese la cantidad de operaciones a realizar: "))

# Utilizamos un bucle while para iterar tantas veces como operaciones se hayan especificado
i = 0
while i < num_operaciones:
    # Preguntamos al usuario si desea realizar un ingreso o una salida de mercadería
    tipo_operacion = input("¿Desea realizar un ingreso (I) o una salida (S) de mercadería?: ")

    # Si el usuario elige un ingreso, aumentamos el stock actual
    if tipo_operacion == "I":
        cantidad = int(input("Ingrese la cantidad de mercadería a ingresar: "))
        stock_actual += cantidad
    # Si el usuario elige una salida, disminuimos el stock actual
    elif tipo_operacion == "S":
        cantidad = int(input("Ingrese la cantidad de mercadería a salir: "))
        stock_actual -= cantidad

    # Aumentamos la variable contadora del bucle
    i += 1

# Mostramos el stock final al usuario
print("El stock final es:", stock_actual)
#********************************************************************
# OTRO EJEMPLO

# Creamos un diccionario para almacenar la información de la mercancía
mercancia = {}

# Inicializamos la variable que llevará el registro del stock actual y las variables para llevar el registro del costo total de entradas y salidas
stock_actual = 0
costo_total_entradas = 0
costo_total_salidas = 0

# Pedimos al usuario que ingrese la cantidad de operaciones a realizar
num_operaciones = int(input("Ingrese la cantidad de operaciones a realizar: "))

# Utilizamos un bucle while para iterar tantas veces como operaciones se hayan especificado
i = 0
while i < num_operaciones:
    # Preguntamos al usuario si desea realizar un ingreso o una salida de mercadería
    tipo_operacion = input("¿Desea realizar un ingreso (I) o una salida (S) de mercadería?: ")

    # Si el usuario elige un ingreso, aumentamos el stock actual y calculamos el costo total de la entrada
    if tipo_operacion == "I":
        cantidad = int(input("Ingrese la cantidad de mercadería a ingresar: "))
        costo_unitario = float(input("Ingrese el costo unitario de la mercadería: "))
        stock_actual += cantidad
        costo_total_entradas += cantidad * costo_unitario
    # Si el usuario elige una salida, disminuimos el stock actual y calculamos el costo total de la salida
    elif tipo_operacion == "S":
        cantidad = int(input("Ingrese la cantidad de mercadería a salir: "))
        costo_unitario = float(input("Ingrese el costo unitario de la mercadería: "))
        stock_actual -= cantidad
        costo_total_salidas += cantidad * costo_unitario

    # Aumentamos la variable contadora del bucle
    i += 1

# Mostramos al usu Mostramos al usuario el costo total de las entradas, las salidas y el saldo final
print("Costo total de entradas:", costo_total_entradas)
print("Costo total de salidas:", costo_total_salidas)
print("Costo total del saldo final:", stock_actual * costo_unitario)




