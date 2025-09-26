import numpy as np

class Lista:
    __Cantidad:int
    __Dimension:int
    __Lista:np.array
    
    def __init__(self, dim=10):
        self.__Cantidad = 0
        self.__Dimension = dim
        self.__Lista = np.full (dim, None, dtype = object)

    def InsertarPorPosicion (self, p, num):
        if self.__Cantidad == 0:
            self.__Lista[self.__Cantidad] = num
            self.__Cantidad += 1
        elif self.__Cantidad == self.__Dimension:
            print ("Lista llena")
        else:
            if self.__Lista[p] == 0:
                self.__Lista[p] = num
                self.__Cantidad += 1
            else:
                for i in range(self.__Dimension -1, p, -1):
                    self.__Lista[i] = self.__Lista[i-1]
                self.__Lista[p] = num
                self.__Cantidad += 1
                
    def Recorrer (self):
        for i in range(self.__Cantidad):
            print(self.__Lista[i])
            
    def SuprimirPorPosicion (self, p):
        if self.__Dimension == 0:
            print ("La lista esta vacia")
        else:
            for i in range(p, self.__Dimension -1):
                self.__Lista[i] = self.__Lista[i + 1]
            self.__Cantidad -= 1
            
    def BuscarPorPosicion (self, num):
        if self.__Dimension == 0:
            print ("La lista esta vacia")
        else:
            print (f"{self.__Lista[num]}")
            
if __name__ == "__main__":
    l=Lista()
    l.InsertarPorPosicion(0, 1)
    l.InsertarPorPosicion(1, 2)
    l.InsertarPorPosicion(2, 3)
    l.InsertarPorPosicion(2, 1)
    l.Recorrer()
    l.SuprimirPorPosicion(2)
    print ("--------------------------------------------------------------")
    l.Recorrer()
    l.BuscarPorPosicion (2)