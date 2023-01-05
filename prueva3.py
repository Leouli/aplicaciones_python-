# Importar las bibliotecas necesarias
import docx2txt
from googletrans import Translator
import os

# Construir la ruta completa del archivo
file_path = os.path.join("C:\\Users\\lenovo\\Documents\\Cv", "filename.docx")

# Cargar el documento Word
text = docx2txt.process(file_path)

# Inicializar el traductor de Google
translator = Translator()

# Traducir el texto del inglés al español
translation = translator.translate(text, dest='es')

# Imprimir la traducción
print(translation.text)
