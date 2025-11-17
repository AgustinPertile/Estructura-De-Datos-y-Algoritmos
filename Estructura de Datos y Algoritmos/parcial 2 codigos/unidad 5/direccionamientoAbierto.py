import numpy as np 

class Hash():
    __Arreglo:np.array
    __Dimension:float
    
    def __init__(self, CantC=10, FactorCarga=0.7):
        self.__Dimension = self.ProximoPrimo(int(CantC // FactorCarga))
        self.__Arreglo = np.empty(self.__Dimension, dtype=object)
        
        
        
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
    
    def insertar(self, clave):
        pos=self.hash(clave)
        aux=pos
        bandera=False
        if self.__tabla[pos]==None:
            self.__tabla[pos]=clave
        elif self.__tabla[pos]==clave:
            print('la clave ya existe')
        else:
            aux=(aux+1)%self.__dimension
            while self.__tabla[aux]!=None and aux!=pos and bandera==False:
                if self.__tabla[aux]==clave:
                    bandera=True
                aux=(aux+1)%self.__dimension
            if aux==pos:
                print('sin espacio')
            elif bandera==True:
                print("clave existente")
            else:
                self.__tabla[aux]=clave
                
    def Recorrer (self):
        for i in range(len(self.__Arreglo)):
            print (f"{self.__Arreglo[i]}")
            
    def Buscar_clave(self, clave):
        pos=self.hash(clave)
        aux=pos
        if self.__Tabla[pos]==None:
            print("la clave no existe en la tabla")
        elif self.__Tabla[pos]==clave:
            print(f'la clave se encuentra en la posicion {pos}')
        else:
            aux=(aux+1)%self.__dimension
            cont=0
            while self.__Tabla[aux]!=clave and aux!=pos:
                aux=(aux+1)%self.__dimension
                cont+=1
            if aux==pos:
                print('la clave no se encuentra en la tabla')
            else:
                print(f"la clave se encuentra en la posicion {aux}")
            
    '''def Buscar (self, dato):
        clave = dato % self.__Dimension
        aux = clave
        cont=0
        if self.__Arreglo[aux] == None:
            print ("Ese dato no esta en la tabla")
        elif self.__Arreglo[aux] == dato:
            print (f"El elemento se encunetra en la posicion: {aux}")
        else:
            aux = (aux+1) % self.__Dimension
            while aux != clave and self.__Arreglo[aux] != dato:
                aux = (aux+1) % self.__Dimension
                cont+=1
            if aux == clave:
                print ("El elemento no existe")
            else:
                print (f"El elemento se ecuentra en la posicion: {aux}")'''
    
    
    '''def Insertar (self, dato):
        clave = dato % self.__Dimension
        aux = clave
        bandera=False
        cont=0
        if self.__Arreglo[aux] == None:   
                self.__Arreglo[aux] = dato
        elif self.__Arreglo[aux] == dato:
            print (f"El elemento {dato} ya existe en la tabla")
        else:
            aux = (aux+1) % self.__Dimension
            while self.__Arreglo[aux] != None and aux != clave and bandera==False:
                if self.__Arreglo[aux] == dato:
                    bandera=True
                cont+=1
                aux = (aux+1) % self.__Dimension
            if aux == clave:
                print ("Tabla llena")
            elif bandera == True:
                print (f"El elemento {dato} ya existe en la tabla")
            else:
                self.__Arreglo[aux] = dato'''
            
            
if __name__ == "__main__":
    h=Hash()
    h.Insertar(10)
    h.Insertar(5)
    h.Insertar(3)
    h.Insertar(10)
    h.Insertar(3)
    h.Insertar(20)
    h.Insertar(20)
    h.Recorrer()
    h.Buscar(20)
                
            
            
        
        