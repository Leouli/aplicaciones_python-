

agenda = {
    "lunes": [],
    "martes": [],
    "miércoles": [],
    "jueves": [],
    "viernes": [],
    "sábado": [],
    "domingo": []
}

def agregar_actividad(dia, hora, descripcion):
  agenda[dia].append((hora, descripcion))

def ver_actividades(dia):
  print(f"Actividades para el día {dia}:")
  for hora, descripcion in agenda[dia]:
    print(f"- A las {hora}: {descripcion}")

def eliminar_actividad(dia, hora):
  for i, (h, descripcion) in enumerate(agenda[dia]):
    if h == hora:
      del agenda[dia][i]
      break
def agregar_actividad(dia, hora, descripcion):
  dia = dia.lower().strip()  # Convertir a minúsculas y eliminar espacios en blanco al inicio y al final
  if dia not in agenda:
    print("Día inválido. Por favor ingrese un día válido.")
    return
  agenda[dia].append((hora, descripcion))
def mostrar_menu():
  print("1. Agregar actividad")
  print("2. Ver actividades de un día")
  print("3. Eliminar actividad")
  print("4. Salir")

while True:
  mostrar_menu()
  opcion = int(input("Elige una opción: "))

  if opcion == 1:
    dia = input("Ingresa el día: ")
    hora = input("Ingresa la hora: ")
    descripcion = input("Ingresa la descripción: ")
    agregar_actividad(dia, hora, descripcion)
  elif opcion == 2:
    dia = input("Ingresa el día: ")
    ver_actividades(dia)
  elif opcion == 3:
    dia = input("Ingresa el día: ")
    hora = input("Ingresa la hora: ")
    eliminar_actividad(dia, hora)
  elif opcion == 4:
    break
  else:
    print("Opción inválida")

    #compila