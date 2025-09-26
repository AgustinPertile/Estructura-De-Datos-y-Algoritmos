import numpy as np

class Cola ():
    __Elementos: np.array
    __Dimension: int
    __Cantidad: int
    __Primero: int
    __Ultimo: int
    
    def __init__ (self, dimension=5):
        self.__Elementos = np.empty(dimension, dtype=int)
        self.__Dimension = dimension
        self.__Cantidad = 0
        self.__Primero = 0
        self.__Ultimo = 0
        
    def Vacia (self):
        return self.__Cantidad == 0
    
    def Llena(self):
        return self.__Cantidad == self.__Dimension
        
    def Insertar (self, elemento):
        if (self.__Cantidad < self.__Dimension):
            self.__Elementos[self.__Ultimo]=elemento
            self.__Ultimo = (self.__Ultimo + 1) % self.__Dimension
            self.__Cantidad += 1
            
    def Suprimir (self):
        if self.Vacia():
            print ("La lista esta vacia")
        else: 
            aux = self.__Elementos[self.__Primero]
            self.__Primero = (self.__Primero + 1) % self.__Dimension
            self.__Cantidad -= 1
            return aux
            
    def Recorrer (self):
        if self.Vacia():
            print ("La lista esta vacia")
        else:
            indice = self.__Primero
            for _ in range (self.__Cantidad):
                print (f"{self.__Elementos[indice]}") 
                indice = (indice + 1) % self.__Dimension
                

            
