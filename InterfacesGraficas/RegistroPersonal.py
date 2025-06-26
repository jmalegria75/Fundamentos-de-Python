from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Registro de Personal")
raiz.resizable(False, False)
raiz.attributes('-toolwindow', True)
raiz.geometry("530x300")

fraPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
fraPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))

#Marco Datos
#-----------------------------------------------------
fraDatos = ttk.Frame(fraPrincipal)
fraDatos.grid(column=0, row=0, sticky=(N, W, E, S))

nombre = StringVar()
aPaterno = StringVar()
aMaterno = StringVar()
correo = StringVar()
movil = StringVar()

estado = StringVar()

ttk.Label(fraDatos, text="Nombre:").grid(column=1, row=1, sticky=(E))
txtNombre = ttk.Entry(fraDatos, width=40, textvariable=nombre)
txtNombre.grid(column=2, row=1, sticky=(W, E))
txtNombre.grid_configure(padx=15, pady=5)

ttk.Label(fraDatos, text="A. Paterno:").grid(column=1, row=2, sticky=(E))
txtAPaterno = ttk.Entry(fraDatos, width=30, textvariable=aPaterno)
txtAPaterno.grid(column=2, row=2, sticky=(W, E))
txtAPaterno.grid_configure(padx=15, pady=5)

ttk.Label(fraDatos, text="A. Materno:").grid(column=1, row=3, sticky=(E))
txtMPaterno = ttk.Entry(fraDatos, width=30, textvariable=aMaterno)
txtMPaterno.grid(column=2, row=3, sticky=(W, E))
txtMPaterno.grid_configure(padx=15, pady=5)

ttk.Label(fraDatos, text="Correo:").grid(column=1, row=4, sticky=(E))
txtCorreo = ttk.Entry(fraDatos, width=30, textvariable=correo)
txtCorreo.grid(column=2, row=4, sticky=(W, E))
txtCorreo.grid_configure(padx=15, pady=5)

ttk.Label(fraDatos, text="Móvil:").grid(column=1, row=5, sticky=(E))
txtMovil = ttk.Entry(fraDatos, width=30, textvariable=movil)
txtMovil.grid(column=2, row=5, sticky=(W, E))
txtMovil.grid_configure(padx=15, pady=5)

#Marco Ocupación
#-----------------------------------------------------

fraOcupacion = ttk.Frame(fraPrincipal)
fraOcupacion.grid(column=1, row=0, sticky=(N, W, E, S))
fraOcupacion.grid_configure(padx=0, pady=45)

ocupacion = StringVar()

optEstudiante = ttk.Radiobutton(fraOcupacion, text="Estudiante", variable=ocupacion, value='Estudiante')
optEstudiante.grid(column=1, row=1, sticky=(W, E))
optEstudiante.grid_configure(padx=30, pady=0)
optEmpleado = ttk.Radiobutton(fraOcupacion, text="Empleado", variable=ocupacion, value='Empleado')
optEmpleado.grid(column=1, row=2, sticky=(W, E))
optEmpleado.grid_configure(padx=30, pady=0)
optDesEmpleado = ttk.Radiobutton(fraOcupacion, text="Desempleado", variable=ocupacion, value='Desempleado')
optDesEmpleado.grid(column=1, row=3, sticky=(W, E))
optDesEmpleado.grid_configure(padx=30, pady=0)

#Marco Aficiones
#-----------------------------------------------------

fraAficiones = ttk.Frame(fraPrincipal)
fraAficiones.grid(column=0, row=1, sticky=(N, W, E, S), pady=20)

aficion = StringVar()

ttk.Label(fraAficiones, text="Aficiones: ").grid(column=1, row=1, sticky=(E), padx=20, pady=0)
chkLeer = ttk.Checkbutton(fraAficiones, text="Leer", variable=aficion, onvalue='leer')
chkLeer.grid(column=1, row=2, sticky=(W, E))
chkLeer.grid_configure(padx=20, pady=0)
chkMusica = ttk.Checkbutton(fraAficiones, text="Música", variable=aficion, onvalue='musica')
chkMusica.grid(column=2, row=2, sticky=(W, E))
chkMusica.grid_configure(padx=20, pady=0)
chkVideojuegos = ttk.Checkbutton(fraAficiones, text="Videojuegos", variable=aficion, onvalue='videojuegos')
chkVideojuegos.grid(column=3, row=2, sticky=(W, E))
chkVideojuegos.grid_configure(padx=20, pady=0)


fraEstados = ttk.Frame(fraPrincipal)
fraEstados.grid(column=1, row=1, sticky=(N, W, E, S), pady=20)
estado = StringVar()
ttk.Label(fraEstados, text="Estados: ").grid(column=0, row=0, sticky=(W))
comboEstados = ttk.Combobox(fraEstados, textvariable=estado)
comboEstados.grid(column=0, row=1, sticky=(N, W, E, S))

comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan", "Zacatecas")

#Marco Botonos
#-----------------------------------------------------

fraBotones = ttk.Frame(fraPrincipal)
fraBotones.grid(column=0, row=2, sticky=(N, W, E, S), padx=20, pady=20)

btnGuardar = ttk.Button(fraBotones, text="Guardar")
btnGuardar.grid(column=1, row=1, sticky=(W))
btnGuardar.grid_configure(padx=0, pady=0)
btnCancelar = ttk.Button(fraBotones, text="Aceptar")
btnCancelar.grid(column=2, row=1, sticky=(E))
btnCancelar.grid_configure(padx=20, pady=0)


for child in raiz.winfo_children():
    child.grid_configure(padx=5, pady=5)

raiz.mainloop()
