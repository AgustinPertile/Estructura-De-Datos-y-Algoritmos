import numpy as np

class Nodo:
    __Dato:int
    __Siguiente:None
    
    def __init__(self, dato):
        self.__Dato = dato
        self.__Siguiente = None
        
    def getDato(self):
        return self.__Dato
    
    def setDato(self, dato):
        self.__Dato = dato
    
    def getSiguiente(self):
        return self.__Siguiente
    
    def setSiguiente(self, sig):
        self.__Siguiente = sig
        
        
class Arreglo:
    __Arreglo:np.array 
    __Dimension:int
    
    def __init__(self, CantC=10, Colisiones=2):
        self.__Dimension = self.ProximoPrimo(CantC // Colisiones)
        self.__Arreglo = np.empty(self.__Dimension, dtype=object)
        
        
    def __hash (self, dato):
        return dato % self.__Dimension
    
    
    def Primo (self, n):
        if n <= 1:
            return False
        for i in range (2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    
    def ProximoPrimo (self, n):
        n += 1
        while not self.Primo(n):
            n += 1
        return n
        

    def Insertar (self, dato):
        clave = self.__hash(dato)
        aux = clave
        cabeza = self.__Arreglo[aux]
        cont=0
        bandera=False
        if cabeza == None:   
            self.__Arreglo[aux] = Nodo(dato) 
        else:
            actual = cabeza
            while actual is not None and bandera == False:
                if actual.getDato() == dato:
                    print(f"El elemento {dato} ya existe en la tabla (posicion{clave})")
                    bandera = True
                actual = actual.getSiguiente()
                cont += 1
            if bandera == False:
                nuevo = Nodo(dato)
                nuevo.setSiguiente(cabeza)
                self.__Arreglo[clave] = nuevo
            print (f"La cantidad de colisiones es de {cont}")
            
            
    def Recorrer(self):
        for i in range(self.__Dimension):
            actual = self.__Arreglo[i]
            if actual is None:
                print(f"[{i}]: -")
            else:
                elems = []
                while actual is not None:
                    elems.append(str(actual.getDato()))
                    actual = actual.getSiguiente()
                print (f"[{i}]: " + " -> ".join(elems))
            
                
    def Buscar(self, dato):
        clave = self.__hash(dato)
        aux=clave
        actual = self.__Arreglo[aux]
        pos = 0
        bandera = False
        if self.__Arreglo[aux] == dato:   
            print (f"El elemento se encuntra en la posicion: {aux}")
        else:
            while actual is not None and bandera == False:
                if actual.getDato() == dato:
                    bandera = True
                actual = actual.getSiguiente()
                pos += 1
            if bandera == False:
                print ("Elemento no encontrado")
            else:
                print (f"El elemento se encuentra en la posicion {aux} del arreglo y en la posicion {pos} de la lista de colisiones") 
    
                
if __name__ == "__main__":
    a=Arreglo()
    a.Insertar(5)
    a.Insertar(10)
    a.Insertar(3)
    a.Insertar(20)
    a.Insertar(10)
    a.Insertar(40)
    a.Insertar(20)
    a.Insertar(15)
    a.Insertar(21)
    a.Recorrer()
    print ("--------------------------------------")
    a.Buscar(25)
    
    