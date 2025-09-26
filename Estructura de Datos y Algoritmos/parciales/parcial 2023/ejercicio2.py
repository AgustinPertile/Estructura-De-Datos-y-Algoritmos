import numpy as np
import random 
class Cola:
    __dato:np.array
    __primero:int
    __ultimo:int
    __dimension:int
    __cantidad:int
    
    def __init__(self, dim=100):
        self.__dato=np.empty(dim, dtype=int)
        self.__primero=0
        self.__ultimo=0
        self.__cantidad=0
        self.__dimension=dim
    
    def vacia(self):
        pass
    def insertar(self):
        pass
    
    def suprimir(self):
        if self.vacia()==0:
            print("La cola esta vacia")
        else:
            aux=self.__dato[self.__primero]
            self.__primero=(self.__primero+1)%self.__dimension
            self.__cantidad-=1
            return aux

def simulacion(self):
    cola=Cola()
    reloj=0
    tsimulacion=300
    empleado=15
    tllegada=10
    cantA=0
    timempoEsperaTotal=0
    cantN=0
    tiempoN=0
    while reloj<tsimulacion:
        n=random.uniform(0.0, 1.0)
        if 0 <= n <= (1 / tllegada):
            cola.insertar(reloj)
            
        if empleado==15 and not cola.vacia():
            solicitante=cola.suprimir()
            tiempoE=reloj-solicitante
            timempoEsperaTotal+=tiempoE
            cantA+=1
            empleado=0
        if empleado<15:
            empleado+=1
        reloj+=1
    
    while not cola.vacia():
        solic=cola.suprimir()
        tiempE=reloj-solic
        tiempoN+=tiempE
        cantN+=1
        
    if cantN>0:
        print(f"el tiempo de espera promedio de los que no fueron atendidos es: {tiempoN/cantN}")
    else:
        print("no quedaron clientes sin atender")
            
            
            
            
    
    
            