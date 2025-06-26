file = open("EjemploArchivo.txt", "w")
file.write("Este es el contenido del archivo.")
file.close()

lista = ["Fresa", "Mango", "Papaya"]
with open("EjemploArchivo.txt", "a")  as file:  # el parametro a es para agregar en el archivo
    for e in lista:
        file.write(e + "\n")
        
print("Lista escrita en el archivo")

lista2 = ["Honda", "Susuki", "BMW"]
with open("EjemploArchivo.txt", "a") as file:
    file.writelines(lista2)

print("Lista2 escrita con writelines.")

#ToDo:  Hacer ejercicios con los diferentes parametros... w, a, etc.

print("---- Imprimir todo el contenido del archivo ----")
with open("EjemploArchivo.txt", "r") as file:
    print(file.read())

print("---- Leer dos lineas y posteriormente 5 caracteres ----")
with open("EjemploArchivo.txt", "r") as file:
    print(file.readline())  #Lee linea por linea y avanza a la siguiente linea
    print(file.readline())
    print(file.readline(5)) # Al pasarle parámetro lee el número de caracteres

print("---- Almacenar el contenido en una lista y mostrar el ultimo elemento ----")
with open("EjemploArchivo.txt", "r") as file:
    contenido = file.readlines()
    print(contenido[-1])



