def nuevo_tema(tema:str):
    print(f"\n----- {tema} -----\n")

if __name__ == "__main__":

    #Operadores Aritmeticos
    nuevo_tema("Operadores aritmeticos")
    print("Operador suma, 5 + 6 = ", 5 + 6)
    print("Operador resta, 10 - 6 = ", 10 - 6)
    print("Operador multiplicacion, 7 * 3 = ", 7 * 3)
    print("Operador división, 7 / 3 = ", 7 / 3)
    print("Operador división entera, 7 // 3 = ", 7 // 3) 
    print("Operador modulo, 7 % 3 = ", 7 % 3) 
    print("Operador cambio de signo, - 3 = ", - 3) 

    #Este es un comentario de una sola linea

    ''' Los 3 apostrofes se usa para comentarios de muchas
        líneas...
    '''

    # Aquí continua con otro contexto, ya no tiene tambulador
    print("Otro mensaje.")

    # ------------------------------------------------
    # --------------  TAREA 1  -----------------------
    # ------------------------------------------------

    #1. Hacer las tablas de vedad
    nuevo_tema("Operadores Logicos")
    print("------------------------------")
    print("/n")
    print("---- Tabla de Verdad AND -----")
    print("True and True : ", True and True)
    print("True and Faalse : ", True and False)
    print("False and True : ", False and True)
    print("False and False : ", False and False)

    print("/n")
    print("---- Tabla de Verdad NOT -----")
    print("Not False : ", not False)
    print("Not True : ", not True)

    print("/n")
    print("---- Tabla de Verdad OR -----")
    print("True or True : ", True or True)
    print("True or Faalse : ", True or False)
    print("False or True : ", False or True)
    print("False or False : ", False or False)

    #2. Ejemplo de cada operador de comparacion
    #Operadores Lógicos
    print("/n")
    nuevo_tema("Operadores de Comparacion")
    print("------------------------------")
    print("/n")
    print("5 == 6 : ", 5 == 6)
    print("5 != 6 : ", 5 != 6)
    print("5 < 6 : ", 5 < 6)
    print("5 <= 6 : ", 5 <= 6)
    print("5 > 6 : ", 5 > 6)
    print("5 >= 6 : ", 5 >= 6)


    #Variables
    nuevo_tema("Variables")
    variable1 = 10
    _variable2 = 6.2547
    variables3 = "Pepe"
    nombreVariable = 8
    nombre_variable = 34.2
    print(variable1, _variable2, variables3, nombreVariable, nombre_variable)
    print("\n")
    a, b, c = 5, 10.8, "Hola"
    print(a)
    print(b)
    print(c)

    #Ejemplo de variable dinámica
    nombre_variable = "Adios"
    print(nombre_variable)

    nuevo_tema("Enteros")
    w = 105
    x = 122343545454556
    y = -58
    z = 0b00110011
    h = 0xFF

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevo_tema("Flotantes")
    x = 1234.56
    print(x, type(x))
    y = -.2584
    print(y, type(y))

    nuevo_tema("Número Complejos")
    x = -46j
    y = 12 + 45j
    z = 2j
    c = y + z
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(c, type(c))

    nuevo_tema("Boleanos")
    x = True
    print(x, type(x))
    y = False
    print(y, type(y)) 

    nuevo_tema("Listas")
    lista = [10, 20.5, "Lista de Python"]
    print(lista, type(lista))
    print(lista[2])
    lista[1] = "Otro dato"
    print(lista)
    lista.append("nuevo dato")
    lista.append(11)
    print(lista)
    lista.insert(0, 1.1)
    print(lista)
    lista.append([3, 4, 5, 6, 7, 8]) # Se puede agregar una lista a otra lista.
    print(lista)
    print(lista[6])
    print(lista[6][4])
    print(lista[3][3])


    nuevo_tema("Tuplas")
    tupla = (25, "Tupla", 1 + 10j)
    print(tupla)
    print(tupla[1])
    #tupla[0] = 0  -> Operación no valida porque la tupla es inmutable o no se pueden cambiar los elementos
    print (tupla)

    nuevo_tema("Conjuntos")
    conjunto = {10, 20, 30, 40, 50, 70}
    print(conjunto)
    #print(conjunto[1]) No se puede acceder a un dato en un conjunto por indice.

    conjunto.add(80)  # Agrega el elemento al inicio
    print(conjunto)
    print(50 in conjunto) # La palabra in busca un elemento en un conjunto.

    nuevo_tema("Diccionarios")
    diccionario = {"Nombre": "Conrado",
                    "Edad": 50,
                    "Telefono": "3312685716",
                    90: 4 + 3j
                    }
    print(diccionario)
    print(diccionario["Telefono"])

    nuevo_tema("Cadenas")
    cadena1 = "Esta es una cadena"
    cadena2 = 'Esto es otra cadena'
    cadena_multilinea = '''Esto es una cadena 
    multilinea,     con tabuladores 
    y 
    saltos de 
    linea '''

    print(cadena1, type(cadena1))
    print(cadena2, type(cadena2))
    print(cadena_multilinea, type(cadena_multilinea))

    cadena3 = "Hola " * 5
    print(cadena3)
    print(cadena1[2:10])
    print(cadena1[:5])
    print(cadena1[5:])
    print(cadena1[:-5])
    print(cadena1[5:])
    print(cadena1[::-1]) #Mostrar las cadenas al revés
