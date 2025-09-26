import numpy as np

class Pila:
    __dato:np.array
    __tope:int
    __dimension:int
    __cantidad:int
    
    def __init__(self, dimension=5):
        self.__dato=np.empty(dimension, dtype=int)
        self.__tope=-1
        self.__dimension=dimension
        self.__cantidad=0
    
    def llena(self):
        return self.__cantidad==self.__dimension
            
    
    def insertar(self, elemento):
        if self.llena():
            print("Pila llena")
        else:
            self.__tope+=1
            self.__dato[self.__tope]=elemento
            self.__cantidad+=1
        