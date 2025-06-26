from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Manejo de Etiquetas")
raiz.geometry("450x400")

etqTexto = ttk.Label(raiz, text="Etiqueta sólo texto y color de fondo", background="lightgray", justify="center")
etqTexto.grid(column=1, row=1, sticky=(N, W, E, S))


#url = "https://ia-examples-jmanuel.s3.us-east-1.amazonaws.com/"
#s3file = "MaestriaIA/Imagenes/gnomes-valentine.png" 

#imagen = PhotoImage(file = url + s3file)
imagen = PhotoImage(file="InterfacesGraficas/logoMBGE.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid(column=1, row=2, sticky=(N, W, E, S))
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="Etiqueta combinada", compound="center")
etqCombinada.grid(column=1, row=3, sticky=(N, W, E, S))
etqCombinada['image'] = imagen

for child in raiz.winfo_children():
    child.grid_configure(padx=5, pady=5)

raiz.mainloop()
