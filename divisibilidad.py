#divisibilidad.py
#aplicacion para saber si hay divisible entre dos numeros
N1 = int(input('introdusca un Numero1 entero : '))
N2 = int(input('introdusca un Numero2 entero : '))
#imprimir los resultados

print(f'la suma es {N1 + N2}')
print(f'la resta es {N1 - N2}')
print(f'la multiplicacion es {N1 * N2}')
print(f'la division es {N1 / N2}')
print(f'la el resto es  {N1 % N2}')
print(f'la el resto es  {N1 % N2}')
resto = N1 % N2
if resto != 0:
    print(f'NO es dibisdible')

else:
    print(f'es dibisdible')

# compila




