#proycomparacionsumas.py
suma1 = 0
suma2 = 0
# solicita valores para la lista 1

x = 1
while x <= 15 :
        valor = int(input('ingrese un valor para la lista1: '))
        suma1 = suma1 + valor
        x = x + 1
x = 1
while x <= 15 :
        valor = int(input('ingrese un valor para la lista2 :'))
        suma2 = suma2 + valor
        x=x+1
# compra los valores acumulados e imprime un mensaje
if suma1>suma2:
   print(f' la lista 1 tiene un mayor valor')
else:
    if suma2>suma1:
        print(f' la lista 2 tiene un mayor valor')
    else:
        print(f' las listas tienen un valor acumulado igual')
