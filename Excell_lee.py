

#Aquí hay un ejemplo sencillo de una aplicación en Python que abre una hoja de cálculo de Excel y lee los datos de una columna:

import openpyxl

# Abre la hoja de cálculo
wb = openpyxl.load_workbook(r'C:\Users\lenovo\Documents\plan_contable.xlsx')

# Selecciona la primera hoja de trabajo
ws = wb['Hoja3']

# Recorre las celdas de la columna A y muestra el valor de cada celda
for row in ws['C']:
    print(row.value)

# Guarda los cambios en la hoja de cálculo
wb.save('plan_contable.xlsx')




