#descuentoscompras.py
# problema del libro N`
# programa para calcular


comp = int(input('ingrese el monto total de sus compras: '))

if comp > 1000:
    desc = comp * 0.20
else:
    desc = 0
tot_pag = comp - desc
print(f'el total a pagar es :', desc)
print(f'el total a pagar es :', tot_pag)

# compila

