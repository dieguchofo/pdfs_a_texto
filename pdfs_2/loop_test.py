# Esto es para testear cómo appendear listas embebidas en json

import json
import os
import fitz

# lista = []
# a_embeber = [["a", "b"], ["c", "d"], ["e", "f", "g", "h"], ["i"], ["j", "k", "l", "m"]]
# contador = 0
# 
# for n in a_embeber:
#     lista.append([])
#     lista[contador].append(a_embeber[contador])
#     contador = contador + 1
# 
# print(lista)

# YA CON PDFS EN EL DIRECTORIO PDFS_2/PDFS

# assign directory
directory = 'pdfs'

contador = 0
textos = []
 
# iterate over files in
# that directory
for filename in os.listdir(directory):
    doc = fitz.open("pdfs/" + filename) # open a document
    textos.append([])
    for page in doc: # iterate the document pages
        text = page.get_text() # get plain text encoded as UTF-8
        textos[contador].append(text)
    contador = contador + 1

print(textos)