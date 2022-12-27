# descuento.py

comp = int(input('ingrese el monto total de sus compras: '))

if comp > 1000:
    desc = comp * 0.20
    print(f' el descuento es :', desc)
else:
    desc = 0
tot_pag = comp - desc
print(f'el total a pagar es ', tot_pag)
# compila
