import tkinter as tk

def agregar(valor):
    entrada.set(entrada.get() + str(valor))

def calcular():
    try:
        #Se usa la función eval para ejecutar la expresón de entrada.
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except Exception:
        entrada.set("Error")

def borrar():
    entrada.set("")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.resizable(False, False)
ventana.geometry("330x380")

# Variable de entrada
entrada = tk.StringVar()

# Campo de entrada
entrada_texto = tk.Entry(ventana, textvariable=entrada, font=("Arial", 20), justify='right', bd=2)
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0)
]

# Creación de los botones en base a la matriz con las propiedades de texto, fila y columna
for (texto, fila, columna) in botones:
    if texto == "=":
        comando = calcular
    elif texto == "C":
        comando = borrar
    else:
        comando = lambda t=texto: agregar(t)

    ancho = 5
    columna_span = 1

    if texto == "=":
        columna_span = 4  # Ocupa toda la fila
        ancho = 27        

    #Si es el boton igual ponerlo de color azul y fuente blanca.
    if texto == "=":
        tk.Button(ventana, text=texto, width=ancho, height=2, font=("Arial", 14), command=comando, bg="steelblue", fg="white").grid(row=fila, column=columna, columnspan=columna_span, padx=1, pady=1)
    else:
        tk.Button(ventana, text=texto, width=ancho, height=2, font=("Arial", 14), command=comando).grid(row=fila, column=columna, columnspan=columna_span, padx=1, pady=1)

ventana.mainloop()