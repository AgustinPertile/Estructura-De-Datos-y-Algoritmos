import numpy as np

class Pila:
    __Elementos: np.array
    __Dimension: int
    __Tope: int
    __Cantidad: int
    
    def __init__ (self, dimension = 5):
        self.__Elementos = np.zeros(dimension, dtype=list)
        self.__Cantidad = 0
        self.__Tope = -1
        self.__Dimension = dimension
        
    def Vacia (self):
        return self.__Tope == -1
        
    def Insertar (self, elemento):
        if self.__Cantidad == self.__Dimension:
            print ("El arreglo esta lleno")
        else:
            self.__Tope += 1
            self.__Elementos[self.__Tope] = elemento
            self.__Cantidad += 1
        
    def Recorrer (self):
        for i in range(self.__Tope, -1, -1):
            print (f"{self.__Elementos[i]}")
            
    def Suprimir (self):
        if self.Vacia():
            print ("La lista esta vacia")
        else:
            self.__Tope -= 1
            self.__Cantidad -= 1
            
   
            
            
        
