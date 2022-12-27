# problema del libro N`
# calcular el promedio de un alumno que tene 7 calificaciones

sum=0
i=1
nom= str(input('ingrese el nombre:'))

while i <= 7:
    calif = int(input('ingrese calificacion {i}: '))
    sum = sum + calif
    i = i + 1
else:
    prom = sum / 7
print(f' el promedio de las calificaciones de {nom} es: ')
print (prom)

# compila