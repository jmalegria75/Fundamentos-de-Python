import pickle

info = [35, 88, 3.14, 16]

#Con pickle guardamos la lista en un archivo binario
with open("./archivos/ArchivoSerial", "wb") as binFile:
    pickle.dump(info, binFile)

print("Archivo binario escrito")


#Con pickle guardamos la lista en un archivo binario
with open("./archivos/ArchivoSerial", "rb") as binFile:
    lista = pickle.load(binFile)
    print(lista)
print("Archivo binario leido y reconstruido")

