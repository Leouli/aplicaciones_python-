# problema del libro N`
#aplicacion para convertir una cantidad de segundos a equivalente en horas, minutos y segundos
N1 = int(input('ingrese la cantidad de segundos a convertir : '))

#imprimir los resultados
resto = N1 % 3600
y = round((resto / 60) , 0)
z = resto % 60
w = round((N1 / 3600) , 0)
print(f'segundos ? : {N1}')
print(f'EQUIVALE A HORAS: {w} ,MINUTOS : {y} Y SEGUNDOS : {z}')

# compila























