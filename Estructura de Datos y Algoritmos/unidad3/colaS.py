import numpy as np
class Cola:
    __arreglo:np.array
    __dimension:int
    __cantidad:int
    __primero:int
    __ultimo:int
    
    def __init__(self, dimension=5):
        self.__arreglo=np.empty(dimension,dtype=int)
        self.__cantidad=0
        self.__primero=0
        self.__ultimo=0
        self.__dimension=dimension
    
    def vacia(self):
        return self.__cantidad==0
    
    def llena(self):
        return self.__cantidad==self.__dimension
    
    def insertar(self, elem):
        if(self.__cantidad<self.__dimension):
            self.__arreglo[self.__ultimo]=elem
            self.__ultimo=(self.__ultimo+1)%self.__dimension
            self.__cantidad+=1
        '''if self.vacia():
            self.__primero+=1
            self.__ultimo+=1
            self.__arreglo[self.__ultimo]=elem
            self.__cantidad+=1
        elif self.llena():
            print("la cola esta llena, no se puede agregar el elemento")
        else:
            self.__arreglo[self.__ultimo]=elem
            self.__ultimo=(self.__ultimo+1)%5
            self.__cantidad+=1'''
    
    def mostrar(self):
        if self.vacia():
            print("cola vacia")
        else:
            indice=self.__primero
            for i in range(self.__cantidad):
                print(f"{self.__arreglo[indice]}")
                indice=(indice+1)%self.__dimension
    
    def suprimir(self):
        if self.vacia()==True:
            return ("La pila está vacía")
        else:
            aux=self.__arreglo[self.__primero]
            self.__primero=(self.__primero+1)%self.__dimension
            self.__cantidad-=1
            return aux

if __name__=="__main__":
    p=Cola()
    p.insertar(1)
    p.insertar(2)
    p.insertar(3)
    p.insertar(4)
    p.insertar(5)
    p.suprimir()
    p.insertar(6)
    p.suprimir()
    p.insertar(7)
    p.mostrar()