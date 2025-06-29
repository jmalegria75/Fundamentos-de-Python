
class Persona:
    def __init__(self, nombre, a_paterno, a_materno, correo, movil, ocupacion, aficion, estado):
        #Definir atributos de la clase
        #Son los que empiezan con self
        self.nombre = nombre
        self.a_paterno = a_paterno
        self.a_materno = a_materno
        self.correo = correo
        self.movil = movil
        self.ocupacion = ocupacion
        self.aficion = aficion
        self.estado = estado

    #region <Métodos Sets>
    def SetNombre(self, nombre):
        self.nombre = nombre

    def SetAPaterno(self, a_paterno):
        self.a_paterno = a_paterno

    def SetAMaterno(self, a_materno):
        self.a_materno = a_materno

    def SetCorreo(self, correo):
        self.correo = correo

    def SetMovil(self, movil):
        self.movil = movil

    def SetOcupacion(self, ocupacion):
        self.ocupacion = ocupacion

    def SetAficion(self, aficion):
        self.aficion = aficion

    def SetEstado(self, estado):
        self.estado = estado

    #endregion

    #region <Métodos Gets>

    def GetNombre(self):  
        return self.nombre
    
    def GetAPaterno(self):  
        return self.a_paterno
    
    def GetAMaterno(self):  
        return self.a_materno

    def GetCorreo(self):  
        return self.correo
    
    def GetMovil(self):  
        return self.movil

    def GetOcupacion(self):  
        return self.ocupacion
    
    def GetAficion(self):  
        return self.aficion
    
    def GetEstado(self):  
        return self.estado
    
    #endregion
    