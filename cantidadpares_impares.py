#cantidadpares_impares.py

    par = 1
    impar = 1
    for i in range(10):
        valor = int(input('ingrese el valor de numeros a ingresar: '))
        if valor % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1

    print('la cantidad de numeros pares es:')
    print(par)
    print(f'la cantidad de numeros inpar es:')
    print(impar)
#no compila