# Msn_resultado.py
#determinar si un alumno aprueba o desaprueba un curso
nom = str(input('ingrese su nombre : '))
calf1 = int(input('ingrese calificacion1 : '))
calf2 = int(input('ingrese calificacion2 : '))
calf3 = int(input('ingrese calificacion3 : '))

# calculo de promedio
prom = (calf1 + calf2 + calf3)

if prom >= 36:
   print(f'alumno aprobado : ' + str(nom))

else:
    print(f' alumno desaprobado : ' + str(nom))
# compila





