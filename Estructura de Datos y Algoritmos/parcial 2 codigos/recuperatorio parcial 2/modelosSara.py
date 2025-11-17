# ====================================================================================
# MOELO 1
# ====================================================================================
#Ejercicio 1 Arbol binario de busqueda
#a)
class Nodo:
    __dato:int
    __izquierdo:None
    __derecho:None
    def __init__(self, dato):
        self.__dato=dato
        self.__izquierdo=None
        self.__derecho=None
        
class Arbol:
    __raiz:Nodo
    def __init__(self):
        self.__raiz=None
    
#b)
    def grado(self, arbol):
        grado=0
        if arbol!=None:
            if arbol.getIzquierdo() != None:
                grado+=1
            if arbol.getDerecho() != None:
                grado+=1
        return grado
    
    def unDescendiente(self, arbol):
        cont=0
        if arbol != None:
            if self.grado(arbol)==1:
                print(f"{arbol.getDato()}")
                cont+=1
            cont+=self.unDescendiente(arbol.getIzquierdo())
            cont+=self.unDescendiente(arbol.getDerecho())
        return cont

#Ejercicio 2 Tabla hashing
#a)
import numpy as np
class Hashing:
    __areaPrimaria:int
    __areaOverflow:int
    __colisiones:int
    __comienzoOverflow:int
    __Tabla:np.array
    __arregloSecundario:np.array
    
    def __init__(self, claves=800, colisiones=4):
        self.__colisiones=colisiones
        self.__areaPrimaria=(claves//colisiones)
        self.__areaOverflow=(20*(claves//colisiones)//100)
        self.__comienzoOverflow=self.__areaPrimaria
        self.__tabla=np.full((self.__areaPrimaria+self.__areaOverflow, colisiones), None)
        self.__arregloSecundario=np.zeros(self.__areaPrimaria+self.__areaOverflow, dtype=int)

#b)
    def hash(self, clave):
        return clave % self.__areaPrimaria
    
#c)
    def insertar(self, clave):
        pos=self.hash(clave)
        bandera=False
        if self.__arregloSecundario[pos]<self.__colisiones:
            self.__tabla[pos , self.__arregloSecundario[pos]]=clave
            self.__arregloSecundario[pos]+=1
        else:
            aux=self.__comienzoOverflow
            while aux<len(self.__tabla) and bandera==False:
                if self.__arregloSecundario[aux]<self.__colisiones:
                    self.__tabla[aux, self.__arregloSecundario[aux]]=clave
                    self.__arregloSecundario[aux]+=1
                    bandera=True
                aux=aux+1
#Ejercicio 3 Digrafo
#a)
class Digrafo:
    __cantVertices:int
    __matriz:np.array
    def __init__(self, vertices):
        self.__cantVertices=vertices
        self.__matriz=np.zeros((vertices, vertices))
        
#b)
    def gradoEntrada(self, vertice):
        grado=0
        for i in range(self.__cantVertices):
            if self.__matriz[i, vertice]>0:
                grado+=1
        return grado
    
    def gradoSalida(self, vertice):
        grado=0
        for i in range(self.__cantVertices):
            if self.__matriz[vertice, i]>0:
                grado+=1
        return grado
    
    def sumidero(self, vertice):
        return self.gradoEntrada(vertice)>0 and self.gradoSalida==0
    
    def sumideros(self):
        for i in range(self.__cantVertices):
            if self.sumidero(i):
                print(f'el vertice {i} es sumidero')

# ====================================================================================
# MOELO 2
# ====================================================================================
#Ejercicio 1 Arbol binario de busqueda
#a)
class Nodo:
    __dato:int
    __izquierdo:None
    __derecho:None
    
    def __init__(self, dato):
        self.__dato=dato
        self.__izquierdo=None
        self.__derecho=None

class Arbol:
    __raiz:Nodo
    def __init__(self):
        self.__raiz=None
        
#b)

    def NivelK(self, arbol, nivel, contN):
        if arbol is None:
            return
        if contN == nivel:
            print(f'el nodo {arbol.getDato()}')
            return
        if contN < nivel:
            self.NivelK(arbol.getIzquierdo(), nivel, contN + 1)
            self.NivelK(arbol.getDerecho(), nivel, contN + 1)
            
#Ejercicio 2 Tabla Hash
#a)
class Nodo:
    __dato:int
    __siguiente:None
    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None
class Hash:
    __tabla:np.array
    __dimension:int
    def __init__(self, claves=1000, colisiones=5):
        self.__dimension=self.proximoPrimo(claves//colisiones)
        self.__tabla=np.empty(self.__dimension, dtype=object)
        
#b)
    def hash(self, clave):
        pos=clave
        strpos=str(pos)
        extraccion=int(strpos[-2:])
        return extraccion%self.__dimension
#c)
    def buscar(self, clave):
        pos=self.hash(clave)
        aux=pos
        actual=self.__tabla[pos]
        bandera=False
        if self.__tabla[pos]==clave:
            print(f'el dato se encuentra en la posicion {pos}')
        else:
            cont=0
            actual=actual.getSiguiente
            while actual!=None and bandera==False:
                if actual.getDato()==clave:
                    bandera=True
                actual=actual.getSiguiente()
                cont+=1
            if bandera==True:
                print(f'la clave se encuentra en la pos {cont} y se encontro en {cont} intentos')
            else:
                print('la clave no se encuentra en la taba')
                
                
#Ejercicio 3 Digrafo
#a)
class Digrafo:
    __matriz:np.array
    __cantVertices:int
    def __init__(self, vertices):
        self.__cantVertices=vertices
        self.__matriz=np.zeros((vertices, vertices))
#b)
    def relaciones(self, destino, origen):
        if not 0<=origen<self.__cantVertices or not 0<=destino<self.__cantVertices:
            print('indices fuera de rango')
        else:
            self.__matriz[origen, destino]=1

# ====================================================================================
# MOELO 3
# ====================================================================================
#Ejercicio 1 Arbol binario de busqueda
#a)
class Nodo:
    __dato:int
    __izquierdo:None
    __derecho:None
    
    def __init__(self, dato):
        self.__dato=dato
        self.__izquierdo=None
        self.__derecho=None

class Arbol:
    __raiz:Nodo
    def __init__(self):
        self.__raiz=None
#b)
    def Terminales(self, arbol, nodo):
        if arbol is None:
            return
        if arbol.getDato()==nodo:
            if self.grado(arbol)==0:
                print(f'{arbol.getDato()}')
            self.Terminales(arbol.getIzquierdo(), nodo)
            self.Terminales(arbol.getDerecho(), nodo)
            return
        if arbol.getDato()>nodo:
            self.Terminales(arbol.getIzquierdo(), nodo)
        else:
            self.Terminales(arbol.getDerecho(), nodo)

#Ejercicio 2 Digrafo
#a)
class Digrafo:
    __matriz:np.array
    __cantVertices:int
    def __init__(self, vertices):
        self.__cantVertices=vertices
        self.__matriz=np.zeros((vertices,vertices))
#b)

    def adyacentes(self, vertice):
        for i in range(self.__cantVertices):
            if self.__matriz[vertice, i]==1:
                print(f"el vertice {i} es adyacente al vertice {vertice}")

#ejercicio 3 Hash
#a)
class hash:
    __tabla:np.array
    __dimension:int
    def __init__(self, claves=500, colisones=10):
        self.__dimension=self.proximoPrimo(claves//colisones)
        self.__tabla=np.empty(self.__dimension, dtype=object)

#b)
    def hash(self, clave):
        pos=clave*clave
        strpos=str(pos)
        cuadradoMedio=int(strpos[-2:])
        return cuadradoMedio%self.__dimension
#c)
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
        
            
