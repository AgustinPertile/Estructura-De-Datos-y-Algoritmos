import numpy as np
from random import random
class Pila:
    __dato:np.array
    __tope:int
    __dimension:int
    __cantidad:int

    def __init__(self, dimension=30):
        self.__dato=np.empty(dimension,dtype=int)
        self.__cantidad=0
        self.__tope=-1
        self.__dimension=dimension
        

    def insertar(self, elem):
        if self.__cantidad==self.__dimension:
            print("lista llena")
        else:
            self.__tope+=1
            self.__dato[self.__tope]=elem
            self.__cantidad+=1
    
    def recorrer(self):
        for i in range(self.__tope, -1, -1):
            print(f"{self.__dato[i]}")

    
    def suprimir(self):
        if self.vacia()==True:
            return ("La pila está vacía")
        else:
            valor = self.__dato[self.__tope]
            self.__tope -= 1
            self.__cantidad -= 1
            return valor
    
    def vacia(self):
        return self.__tope==-1
    
    def vaciaa(self):
        
        if self.vacia():
            print("pila vacia")
        else:print("pila no vacia")
        

    
            
        
        
        
    
if __name__=="__main__":
    p=Pila()
    '''p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.insertar(4)
    p.insertar(5)
    p.recorrer()'''
    #p.convercion(2)
    p.escalera(7)
    
    