#Kardex.py
class Producto:
    def __init__(self, cantidad, precio_unitario, precio_total):
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.precio_total = precio_total


class Almacen:
    def __init__(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial
        self.entradas = 0
        self.salidas = 0
        self.saldo_actual = saldo_inicial

    def registrar_entrada(self, cantidad, precio_unitario):
        precio_total = cantidad * precio_unitario
        self.entradas += precio_total
        self.saldo_actual += precio_total

    def registrar_salida(self, cantidad, precio_unitario):
        precio_total = cantidad * precio_unitario
        self.salidas += precio_total
        self.saldo_actual -= precio_total

    def ver_saldo(self):
        print(f"Saldo inicial: {self.saldo_inicial}")
        print(f"Entradas: {self.entradas}")
        print(f"Salidas: {self.salidas}")
        print(f"Saldo actual: {self.saldo_actual}")


def menu():
    almacen = Almacen(1000)  # saldo inicial de 1000

    while True:
        print("1. Registrar entrada de mercadería")
        print("2. Registrar salida de mercadería")
