from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import csv
import os

class Ventana:

    def __init__(self):

        self.raiz = Tk()
        self.raiz.title("Listado de Personal")
        self.raiz.resizable(False, False)
        self.raiz.attributes('-toolwindow', True)
        self.raiz.geometry("850x330") 
        
        self.fraPrincipal = ttk.Frame(self.raiz, padding="3 3 12 12")
        self.fraPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))

        #region <Marco Listado> 
        #-----------------------------------------------------
        self.fraListado = ttk.Frame(self.fraPrincipal)
        self.fraListado.grid(column=0, row=0, sticky=(N, W, E, S))

        self.grdLista = ttk.Treeview(self.fraListado, columns=("Nombre", "A. Paterno", "A. Materno", "Correo", "Movil", "Ocupacion", "Aficion", "Estado"), show="headings")

    def CrearInterface(self):
       
        # Definir encabezados
        self.grdLista.heading("Nombre", text="Nombre")
        self.grdLista.heading("A. Paterno", text="A. Paterno")
        self.grdLista.heading("A. Materno", text="A. Materno")
        self.grdLista.heading("Correo", text="Correo")
        self.grdLista.heading("Movil", text="Móvil")
        self.grdLista.heading("Ocupacion", text="Ocupación")
        self.grdLista.heading("Aficion", text="Afición")
        self.grdLista.heading("Estado", text="Estado")

        # Definir el ancho de cada columna
        self.grdLista.column("Nombre", width=120)
        self.grdLista.column("A. Paterno", width=100)
        self.grdLista.column("A. Materno", width=100)
        self.grdLista.column("Correo", width=150)
        self.grdLista.column("Movil", width=70)
        self.grdLista.column("Ocupacion", width=100)
        self.grdLista.column("Aficion", width=100, anchor="center")
        self.grdLista.column("Estado", width=50, anchor="center")

        # Mostrar tabla
        self.grdLista.pack(padx=10, pady=10, fill="both", expand=True)

        #endregion

        #region <Marco Botonos> 
        #-----------------------------------------------------

        fraBotones = ttk.Frame(self.fraPrincipal)
        fraBotones.grid(column=0, row=2, sticky=(N, W, E, S), padx=20, pady=20)

        btnGuardar = ttk.Button(fraBotones, text="Mostrar Datos", command=self.Mostrar)
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

    def limpiar_Listado(self):
        for fila in self.grdLista.get_children():
            self.grdLista.delete(fila)

    def Mostrar(self):
        #Mandamos llamar 
        archivo = "./RegistroPersonas/personas.txt"

        # Vamos a validar que existe el archivo personas.txt 
        if not os.path.exists(archivo):
            messagebox.showerror("Información", "Aún no existe un archivo de personas para leer los datos.")
            return

        with open(archivo, newline='', encoding='utf-8') as file:
            personas = csv.reader(file)
            encabezados = next(personas)

            #Limpiar listado
            self.limpiar_Listado()

            contador = 0
            for persona in personas:
                self.grdLista.insert("", END, values=persona)
                contador += 1
            
            messagebox.showinfo("Información", f"Se encontraron {contador} registros.")

if __name__ == "__main__":
    
    #Iniciamos la clase Ventana
    cVentana = Ventana()
    cVentana.CrearInterface()    
