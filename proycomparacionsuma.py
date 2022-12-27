#proycomparacionsuma.py
suma1=0
suma2=0
x=1
print(f'carga de la primera lista')
while x<=15:
    valor=int(input('ingrese un valor:'))
    suma1=suma1+1
    x=x+1
x=1
print(f'carga de la segunda lista')
while x<=15:
    valor=int(input('ingrese un valor:'))
    suma2=suma2+1
    x=x+1
if suma1>suma2:
    print(f'la lista 1 tiene un valor acumulado mayor')
else:
    if suma2>suma1:
        print(f'la lista 2 tiene un valor acumulado mayor')
    else:
        print(f'las listas tienen un valor acumulado igual')

        # compila - falta revisar