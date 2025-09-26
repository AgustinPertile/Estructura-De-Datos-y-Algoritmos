import numpy as np

class Lista:
    __Cantidad:int
    __Dimension:int
    __Lista:np.array
    
    def getCantidad(self):
        return self.__Cantidad
    
    def getDimension(self):
        return self.__Dimension
    
    def __init__(self, dim=10):
        self.__Cantidad = 0
        self.__Dimension = dim
        self.__Lista = np.full (dim, None, dtype = Contacto)
    
    def InsertarPorContenido (self, nom, tel):
        if self.__Cantidad == 0:
            self.__Lista[self.__Cantidad] = Contacto(nom, tel)
            self.__Cantidad += 1
        elif self.__Cantidad == self.__Dimension:
            print ("Lista llena")
        else:
            if l.BuscarPorContenido (tel) == 1:
                contacto = Contacto(nom, tel)  
                i=0
                while i < self.__Cantidad and self.__Lista[i].getNombre() < contacto.getNombre():
                    i+=1
                for j in range(self.__Cantidad, i, -1):
                    self.__Lista[j] = self.__Lista[j-1]
                self.__Lista[i] = contacto
                self.__Cantidad += 1
                
    def Recorrer (self):
        for i in range(self.__Cantidad):
            print(self.__Lista[i])
            
    def SuprimirPorContenido (self, dato):
        if self.__Dimension == 0:
            print ("La lista esta vacia")
        else:
            i=0
            while i < self.__Cantidad and self.__Lista[i].getNombre() != dato:
                i+=1
            if i == self.__Cantidad:
                print ("No se encontro el elemento")
            else:
                for j in range(i, self.__Dimension -1):
                    self.__Lista[j] = self.__Lista[j + 1]
                self.__Cantidad -= 1
                
    def BuscarPorContenido (self, dato):
        if self.__Cantidad == 0:
            print ("La lista esta vacia")
        else: 
            i=0
            while i < self.__Cantidad and self.__Lista[i].getTelefono() != dato:
                i+=1
            if i == self.__Cantidad:
                return 1
            else:
                print ("El contacto ya existe")
        
    def Buscar (self, nom):
        i=0
        while i<self.__Cantidad and self.__Lista[i].getNombre()!=nom:
            i+=1
        if i == self.__Cantidad:
            print(f"el contacto no existe")
        else:
            print(f"{self.__Lista[i].getTelefono()}")
            
        
        
        
        
class Contacto :
    __Nombre: str 
    __Telefono: int
    
    def __init__ (self, nom, tel):
        self.__Nombre = nom
        self.__Telefono = tel
        
    def getNombre (self):
        return self.__Nombre
    
    def getTelefono (self):
        return self.__Telefono
    
    def __str__(self):
        return f"Nombre: {self.__Nombre}, Teléfono: {self.__Telefono}"
             
                
                
if __name__ == "__main__":
    l=Lista()
    #l.InsertarPorContenido(1)
    #l.InsertarPorContenido(2)
    #l.InsertarPorContenido(3)
    #l.InsertarPorContenido(5)
    #l.InsertarPorContenido(4)
    #l.Recorrer()
    #l.SuprimirPorContenido (5)
    #print ("--------------------------------------------------------------")
    #l.Recorrer()
    #l.BuscarPorContenido (5)
    l.InsertarPorContenido ("Andrea", 12345)
    l.InsertarPorContenido ("Leonel", 24589)
    l.InsertarPorContenido ("Agustin", 36985)   
    l.Recorrer() 
    print ("--------------------------------------------------------------")
    #l.InsertarPorContenido ("Banana", 36985)  
    l.SuprimirPorContenido ("Leonel")
    l.Recorrer()
    l.Buscar("Agustin")
    l.Recorrer ()
    