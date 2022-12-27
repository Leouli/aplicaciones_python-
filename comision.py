# problema del libro N` 2
# programa para calcular comisiones y pago total

sb = int(input('ingrese sueldo base : '))
v1 = int(input('ingrese la venta1 : '))
v2 = int(input('ingrese un venta2 : '))
v3 = int(input('ingrese un venta3 : '))


tot_vta = v1 + v2 + v3
com = tot_vta * 0.10
t_pag = sb + com

#el total de pago y la com es

print(f'el total de venta es : {v1 + v2 + v3}')
print(f'la comision es : {tot_vta * 0.10}')
print(f'el total de pago es : {sb + com}')

# compila
