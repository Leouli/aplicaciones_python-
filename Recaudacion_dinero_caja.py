#Recaudacion_dinero_caja.py

# Pedimos al usuario que ingrese el número de billetes
r = int(input("Ingrese el número de billetes de 200 soles: "))
s = int(input("Ingrese el número de billetes de 100 soles: "))
t = int(input("Ingrese el número de billetes de 20 soles: "))
u = int(input("Ingrese el número de billetes de 10 soles: "))


# Pedimos al usuario que ingrese las monedas
v = int(input("Ingrese el número de monedas de 5 soles: "))
w = int(input("Ingrese el número de monedas de 2 soles: "))
x = int(input("Ingrese el número de monedas de 1 sol: "))
y = int(input("Ingrese el número de monedas de 0.20 centavos: "))
z = int(input("Ingrese el número de monedas de 0.10 centavos: "))

# Calculamos el monto total de dinero recaudado
total = (r * 200) + (s * 100) + (t * 20) + (u * 10) + (v * 5) + (w * 2) + (x * 1) + (y * 0.2) + (z * 0.1)

# Mostramos el monto total de dinero recaudado al usuario
print("El monto total de dinero recaudado es:", total)