#interes.py
#problema del libro N`
# programa para calcular
'''
#rama para calcular el dinero que genera el capital

interes = float(input('ingrese el precio del interes: '))
cap1 = int(input('ingrese el capital: '))

cap2 = cap1 * interes
# generar el calculo


if cap2 > 7000:

    print ('el capital final es' + srt(cap2))

else:

    print('El capital final 2 es' + str(cap2 + interes))

'''


capital1 = input(('Ingrese su capital'))
interesAnual = input(('Ingrese su interes anual'))
capital2 = capital1 + ((capital1 * interesAnual/100))

if capital2 > 7000:
    print('Su capital nuevo se contará a partir de 7000')


# No compila