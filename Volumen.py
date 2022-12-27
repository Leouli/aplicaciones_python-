#Volumen.py
def volumen_cono(r, h):
  volumen = (math.pi * r**2 * h) / 3
  return volumen

# Ejemplo de uso
radio = 3
altura = 5
vol = volumen_cono(radio, altura)
print(f"El volumen del cono es {vol:.2f}")


# para el calcul del volumen de un cubo + el volumen de ssuna piramide

def volumen_cubo(lado):
  volumen = lado**3
  return volumen

def volumen_piramide(lado, ancho, altura):
  volumen = (lado * ancho * altura) / 3
  return volumen

# Ejemplo de uso
lado = 3
vol_cubo = volumen_cubo(lado)
vol_piramide = volumen_piramide(lado, lado, lado)
print(f"El volumen del cubo es {vol_cubo} y el volumen de la pirámide es {vol_piramide}")
