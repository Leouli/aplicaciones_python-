#planilla_remun.py
#import math

class Trabajador:
    def __init__(self, sueldo, bonificacion_costo_vida, bonificacion_especial):
        self.sueldo = sueldo
        self.bonificacion_costo_vida = bonificacion_costo_vida
        self.bonificacion_especial = bonificacion_especial
        self.total_remuneracion = self.calcular_total_remuneracion()
        self.retenciones = self.calcular_retenciones()
        self.deducciones = self.calcular_deducciones()
        self.neto_a_pagar = self.calcular_neto_a_pagar()

    def calcular_total_remuneracion(self):
        total = self.sueldo + self.bonificacion_costo_vida + self.bonificacion_especial
        return round(total, 2)

    def calcular_retenciones(self):
        snp = self.sueldo * 0.09
        ipps = self.sueldo * 0.03
        impuesto_renta = self.sueldo * 0.1
        total = snp + ipps + impuesto_renta
        return round(total, 2)

    def calcular_deducciones(self):
        ipss = self.sueldo * 0.03
        fanavi = self.sueldo * 0.01
        senati = self.sueldo * 0.005
        accidentes_trabajo = self.sueldo * 0.005
        total = ipss + fanavi + senati + accidentes_trabajo
        return round(total, 2)

    def calcular_neto_a_pagar(self):
        total = self.total_remuneracion - self.retenciones - self.deducciones
        return round(total, 2)

def main():
    sueldo = float(input("Ingrese el sueldo del trabajador: "))
    bonificacion_costo_vida = float(input("Ingrese la bonificación por el costo de vida del trabajador: "))
    bonificacion_especial = float(input("Ingrese la bonificación especial del trabajador: "))
    trabajador = Trabajador(sueldo, bonificacion_costo_vida, bonificacion_especial)
    print("Total de remuneración:", trabajador.total_remuneracion)
    print("Retenciones:", trabajador.retenciones)

