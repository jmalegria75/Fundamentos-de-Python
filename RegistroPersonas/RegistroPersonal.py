from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import csv
import os
import Persona

class Ventana:

    def __init__(self, pPersona:Persona):

        self.raiz = Tk()
        self.raiz.title("Registro de Personal")
        self.raiz.resizable(False, False)
        self.raiz.attributes('-toolwindow', True)
        self.raiz.geometry("530x300") 
        
        self.nombre = StringVar()
        self.a_paterno = StringVar()
        self.a_materno = StringVar()
        self.correo = StringVar()
        self.movil = StringVar()
        self.ocupacion = StringVar()
        self.aficion = StringVar()
        self.estado = StringVar()

        self.cPersona = pPersona 

    def CrearInterface(self):

        fraPrincipal = ttk.Frame(self.raiz, padding="3 3 12 12")
        fraPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))

        #region <Marco Datos> 
        #-----------------------------------------------------
        fraDatos = ttk.Frame(fraPrincipal)
        fraDatos.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(fraDatos, text="Nombre:").grid(column=1, row=1, sticky=(E))
        txtNombre = ttk.Entry(fraDatos, width=40, textvariable= self.nombre)
        txtNombre.grid(column=2, row=1, sticky=(W, E))
        txtNombre.grid_configure(padx=15, pady=5)

        ttk.Label(fraDatos, text="A. Paterno:").grid(column=1, row=2, sticky=(E))
        txtAPaterno = ttk.Entry(fraDatos, width=30, textvariable=self.a_paterno)
        txtAPaterno.grid(column=2, row=2, sticky=(W, E))
        txtAPaterno.grid_configure(padx=15, pady=5)
        
        ttk.Label(fraDatos, text="A. Materno:").grid(column=1, row=3, sticky=(E))
        txtMPaterno = ttk.Entry(fraDatos, width=30, textvariable=self.a_materno)
        txtMPaterno.grid(column=2, row=3, sticky=(W, E))
        txtMPaterno.grid_configure(padx=15, pady=5)

        ttk.Label(fraDatos, text="Correo:").grid(column=1, row=4, sticky=(E))
        txtCorreo = ttk.Entry(fraDatos, width=30, textvariable=self.correo)
        txtCorreo.grid(column=2, row=4, sticky=(W, E))
        txtCorreo.grid_configure(padx=15, pady=5)

        ttk.Label(fraDatos, text="Móvil:").grid(column=1, row=5, sticky=(E))
        txtMovil = ttk.Entry(fraDatos, width=30, textvariable=self.movil)
        txtMovil.grid(column=2, row=5, sticky=(W, E))
        txtMovil.grid_configure(padx=15, pady=5)
        #endregion

        #region <Marco Ocupación> 
        #-----------------------------------------------------

        fraOcupacion = ttk.Frame(fraPrincipal)
        fraOcupacion.grid(column=1, row=0, sticky=(N, W, E, S))
        fraOcupacion.grid_configure(padx=0, pady=45)

        optEstudiante = ttk.Radiobutton(fraOcupacion, text="Estudiante", variable=self.ocupacion, value='Estudiante')
        optEstudiante.grid(column=1, row=1, sticky=(W, E))
        optEstudiante.grid_configure(padx=30, pady=0)
        optEmpleado = ttk.Radiobutton(fraOcupacion, text="Empleado", variable=self.ocupacion, value='Empleado')
        optEmpleado.grid(column=1, row=2, sticky=(W, E))
        optEmpleado.grid_configure(padx=30, pady=0)
        optDesEmpleado = ttk.Radiobutton(fraOcupacion, text="Desempleado", variable=self.ocupacion, value='Desempleado')
        optDesEmpleado.grid(column=1, row=3, sticky=(W, E))
        optDesEmpleado.grid_configure(padx=30, pady=0)
        #endregion

        #region <Marco Aficiones> 
        #-----------------------------------------------------

        fraAficiones = ttk.Frame(fraPrincipal)
        fraAficiones.grid(column=0, row=1, sticky=(N, W, E, S), pady=20)

        ttk.Label(fraAficiones, text="Aficiones: ").grid(column=1, row=1, sticky=(E), padx=20, pady=0)
        chkLeer = ttk.Checkbutton(fraAficiones, text="Leer", variable=self.aficion, onvalue='leer')
        chkLeer.grid(column=1, row=2, sticky=(W, E))
        chkLeer.grid_configure(padx=20, pady=0)
        chkMusica = ttk.Checkbutton(fraAficiones, text="Música", variable=self.aficion, onvalue='musica')
        chkMusica.grid(column=2, row=2, sticky=(W, E))
        chkMusica.grid_configure(padx=20, pady=0)
        chkVideojuegos = ttk.Checkbutton(fraAficiones, text="Videojuegos", variable=self.aficion, onvalue='videojuegos')
        chkVideojuegos.grid(column=3, row=2, sticky=(W, E))
        chkVideojuegos.grid_configure(padx=20, pady=0)
        #endregion

        #region <Marco Estados>
        #-----------------------------------------------------

        fraEstados = ttk.Frame(fraPrincipal)
        fraEstados.grid(column=1, row=1, sticky=(N, W, E, S), pady=20)

        ttk.Label(fraEstados, text="Estados: ").grid(column=0, row=0, sticky=(W))
        comboEstados = ttk.Combobox(fraEstados, textvariable=self.estado)
        comboEstados.grid(column=0, row=1, sticky=(N, W, E, S))

        comboEstados['values'] = ("Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua",
                                "Ciudad de México", "Coahuila", "Colima", "Durango", "Estado de México", "Guanajuato", "Guerrero",
                                "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro",
                                "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz",
                                "Yucatán", "Zacatecas")
        #endregion

        #region <Marco Botonos> 
        #-----------------------------------------------------

        fraBotones = ttk.Frame(fraPrincipal)
        fraBotones.grid(column=0, row=2, sticky=(N, W, E, S), padx=20, pady=20)

        btnGuardar = ttk.Button(fraBotones, text="Guardar", command=self.Guardar)
        btnGuardar.grid(column=1, row=1, sticky=(W))
        btnGuardar.grid_configure(padx=0, pady=0)
        btnCancelar = ttk.Button(fraBotones, text="Cancelar", command=self.cerrar_ventana)
        btnCancelar.grid(column=2, row=1, sticky=(E))
        btnCancelar.grid_configure(padx=20, pady=0)
        #endregion

        for child in self.raiz.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.raiz.mainloop()

    def cerrar_ventana(self):
        self.raiz.destroy()  # Cierra la ventana principal

    def Guardar(self):

        #Mandamos llamar 
        archivo = "./RegistroPersonas/personas.txt"

        # Vamos a crear el archivo con encabezados 
        if not os.path.exists(archivo):
            with open(archivo, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Nombre', 'A. Paterno', 'A. Materno', 'Correo', 'Móvil', 'Ocupación', 'Afición', 'Estado'])

        #Asignar datos a la clase
        self.cPersona.SetNombre(self.nombre.get())
        self.cPersona.SetAPaterno(self.a_paterno.get())
        self.cPersona.SetAMaterno(self.a_materno.get())
        self.cPersona.SetCorreo(self.correo.get())
        self.cPersona.SetMovil(self.movil.get())
        self.cPersona.SetOcupacion(self.ocupacion.get())
        self.cPersona.SetAficion(self.aficion.get())
        self.cPersona.SetEstado(self.estado.get())

        #Agrega los datos al archivo 
        with open(archivo, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([self.cPersona.GetNombre(), self.cPersona.GetAPaterno(), self.cPersona.GetAMaterno(), self.cPersona.GetCorreo(), self.cPersona.GetMovil(), self.cPersona.GetOcupacion(), self.cPersona.GetAficion(), self.cPersona.GetEstado()])

            messagebox.showinfo("Información", "Los datos de la persona se han guadado con éxito.")

if __name__ == "__main__":

    #Iniciamos la clase Persona 
    cPersona = Persona.Persona("","","","","","","","")
    
    #Iniciamos la clase Ventana
    cVentana = Ventana(cPersona)
    cVentana.CrearInterface()    
