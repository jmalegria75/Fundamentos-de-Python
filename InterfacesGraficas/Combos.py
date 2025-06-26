from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Manejo de Cuadros combinados (Combos)")
raiz.geometry("430x450")

estado = StringVar()

comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.grid(column=1, row=1, sticky=(N, W, E, S))

comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan", "Zacatecas")

for child in raiz.winfo_children():
    child.grid_configure(padx=5, pady=5)

raiz.mainloop()
