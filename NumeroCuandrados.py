
#NumeroCuandrados.py
l = int(input("Ingrese is longitud del cuadrado mayor:" ))
b = int(input("Ingrese la anchura del cuadrado mayor: " ))

#Luego, pedimos al usuario que ingrese la longitud y anchura
# del cuadrado pequeño

a = int(input("Ingrese la longitud del cuadrado pequeño: "))
b = int(input("Ingrese la anchura del cuadrado pequeñob: "))

#finalmente usamos la operacion matematica simple para calcular ;
# a cantidad la cantidad de cuadrados peque;os que caben em el cuadrado mayor

cuadrados_pequenos = (1 * b) / (a* b)

# Imprimimos el resultado en pantalla

print("En un cuadrado de longitud", 1, "y anchura", b, "caben",
cuadrados_pequenos, "cuadrados pequeños de longitud", a, "y anchura", b)
# pendiente de compilacion
