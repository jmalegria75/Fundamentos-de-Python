from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Inicio de Sesión")
raiz.geometry("300x150")

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0, weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

usuario = StringVar()
contrasenia = StringVar()

txtUsuario = ttk.Entry(marcoPrincipal, width=30, textvariable=usuario)
txtUsuario.grid(column=2, row=1, sticky=(W, E))

txtContrasenia = ttk.Entry(marcoPrincipal, width=30, textvariable=contrasenia)
txtContrasenia.grid(column=2, row=2, sticky=(W, E))

ttk.Label(marcoPrincipal, text="Usuario:").grid(column=1, row=1, sticky=(E))
ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=1, row=2, sticky=E)

ttk.Button(marcoPrincipal, text="Ingresar").grid(column=2, row=3, sticky=(E))

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

txtUsuario.focus()

raiz.mainloop()
