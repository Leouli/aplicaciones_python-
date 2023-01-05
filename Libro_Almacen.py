# Creamos un diccionario para almacenar la información de la mercancía
mercancia = {}

# Creamos variables para llevar un registro del stock
stock_ingresos = 0
stock_salidas = 0
stock_actual = 0

# Pedimos el ingreso de mercadería o saldo inicial de mercadería
print("Ingreso de mercadería o saldo inicial de mercadería")
print("Ingresa la cantidad de mercadería:")
cantidad = int(input())
print("Ingresa el costo unitario de la mercadería:")
costo_unitario = float(input())
costo_total = cantidad * costo_unitario

# Agregamos la información a nuestro diccionario y actualizamos el stock
mercancia['ingresos'] = {'cantidad': cantidad, 'costo_unitario': costo_unitario, 'costo_total': costo_total}
stock_ingresos += cantidad
stock_actual += cantidad

# Pedimos el ingreso de mercadería a almacén
print("Ingreso de mercadería a almacén")
print("Ingresa la cantidad de mercadería:")
cantidad = int(input())
print("Ingresa el costo unitario de la mercadería:")
costo_unitario = float(input())
costo_total = cantidad * costo_unitario

# Agregamos la información a nuestro diccionario y actualizamos el stock
mercancia['ingresos_almacen'] = {'cantidad': cantidad, 'costo_unitario': costo_unitario, 'costo_total': costo_total}
stock_ingresos += cantidad
stock_actual += cantidad

# Pedimos la salida de mercadería de almacén
print("Salida de mercadería de almacén")
print("Ingresa la cantidad de mercadería:")
cantidad = int(input())
print("Ingresa el costo unitario de la mercadería:")
costo_unitario = float(input())
costo_total = cantidad * costo_unitario

# Agregamos la información a nuestro diccionario y actualizamos el stock
mercancia['salidas_almacen'] = {'cantidad': cantidad, 'costo_unitario': costo_unitario, 'costo_total': costo_total}
stock_salidas += cantidad
stock_actual -= cantidad

# Mostramos los totales de mercadería que ingresó
# Mostramos los totales de mercadería que ingresó
print("Totales de mercadería que ingresó")
print("Cantidad:", mercancia['ingresos']['cantidad'] + mercancia['ingresos_almacen']['cantidad'])
print("Precio unitario:", mercancia['ingresos']['costo_unitario'])
print("Precio total:", mercancia['ingresos']['costo_total'] + mercancia['ingresos_almacen']['costo_total'])

# Mostramos los totales de mercadería que salió
print("Totales de mercadería que salió")
print("Cantidad:", mercancia['salidas_almacen']['cantidad'])
print("Precio unitario:", mercancia['salidas_almacen']['costo_unitario'])
print("Precio total:", mercancia['salidas_almacen']['costo_total'])

# Mostramos el saldo de mercadería que queda
print("Saldo de mercadería que queda")
print("Cantidad:", stock_actual)
print("Precio unitario:", mercancia['ingresos']['costo_unitario'])
print("Precio total:", stock_actual * mercancia['ingresos']['costo_unitario'])

