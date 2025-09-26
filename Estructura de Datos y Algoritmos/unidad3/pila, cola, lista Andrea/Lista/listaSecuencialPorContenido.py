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
        self.__Lista = np.full (dim, None, dtype = object)
    
    def InsertarPorContenido (self, dato):
        if self.__Cantidad == 0:
            self.__Lista[self.__Cantidad] = dato
            self.__Cantidad += 1
        elif self.__Cantidad == self.__Dimension:
            print ("Lista llena")
        else:
            i=0
            while i < self.__Cantidad and self.__Lista[i] < dato:
                i+=1
            if self.__Lista[i] == 0:
                self.__Lista[i] = dato
                self.__Cantidad += 1
            else:
                for j in range(self.__Dimension -1, i, -1):
                    self.__Lista[j] = self.__Lista[j-1]
                self.__Lista[i] = dato
                self.__Cantidad += 1
                
    def Recorrer (self):
        for i in range(self.__Cantidad):
            print(self.__Lista[i])
            
    def SuprimirPorContenido (self, dato):
        if self.__Dimension == 0:
            print ("La lista esta vacia")
        else:
            i=0
            while i < self.__Cantidad and self.__Lista[i] != dato:
                i+=1
            if i == self.__Cantidad:
                print ("No se encontro el elemento")
            else:
                for j in range(i, self.__Dimension -1):
                    self.__Lista[j] = self.__Lista[j + 1]
                self.__Cantidad -= 1
                
    def BuscarPorContenido (self, dato):
        if self.__Dimension == 0:
            print ("La lista esta vacia")
        else: 
            i=0
            while i < self.__Cantidad and self.__Lista[i] != dato:
                i+=1
            if i == self.__Cantidad:
                print ("El elemento ya existe")
            else:
                return 1
                
                
                
if __name__ == "__main__":
    l=Lista()
    l.InsertarPorContenido(1)
    l.InsertarPorContenido(2)
    l.InsertarPorContenido(3)
    l.InsertarPorContenido(5)
    l.InsertarPorContenido(4)
    l.Recorrer()
    l.SuprimirPorContenido (5)
    print ("--------------------------------------------------------------")
    l.Recorrer()
    l.BuscarPorContenido (5)