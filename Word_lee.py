import os
import docx2txt
# Construir la ruta completa del archivo
file_path = os.path.join("C:\\Users\\lenovo\\Documents\\Cv\\", "file.docx")

# Cargar el documento Word
text = docx2txt.process(file_path)

# Imprimir el contenido del documento en la consola
print(text)
