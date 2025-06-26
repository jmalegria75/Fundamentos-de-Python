from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Manejo de Botónes")
raiz.geometry("430x450")

boton = ttk.Button(raiz, text="Sólo Botón")
boton.grid(column=1, row=1, sticky=(N, W, E, S))

imagen = PhotoImage(file="InterfacesGraficas/logoMBGE.png")

btnImagen = ttk.Button(raiz)
btnImagen.grid(column=1, row=2, sticky=(N, W, E, S))
btnImagen['image'] = imagen

btnCombinada = ttk.Button(raiz, text="Botón combinado", compound="bottom")
btnCombinada.grid(column=1, row=3, sticky=(N, W, E, S))
btnCombinada['image'] = imagen

chkBoton = ttk.Checkbutton(raiz, text="Opcion 1")
chkBoton.grid(column=1, row=4, sticky=(N, W, E, S))

for child in raiz.winfo_children():
    child.grid_configure(padx=15, pady=5)

raiz.mainloop()
