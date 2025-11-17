# ====================================================================================
# Parcial 2
# ====================================================================================
    
#Ejercicio 1 arbol binario de busqueda
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
            if arbol.getizquierdo()!=None:
                grado+=1
            if arbol.getDerecho()!=None:
                grado+=1
            return grado
        
    def descendientes(self, arbol, nodo):
        if arbol!=None:
            if nodo==arbol.getDato():
                cantDescendientes=self.grado(arbol)
                return cantDescendientes
            if nodo<arbol.getDato():
                self.descendientes(arbol.getIzquierdo(), nodo)
            else:
                self.descendientes(arbol.getDerecho(), nodo)
#c)
#O(n)=logaritmico T(n)=n/2

#Ejercicio 2 Digrafo
#a)
import numpy as np
class Digrafo:
    __Matriz:np.array
    __cantVertices:int
    
    def __init__(self, vertices):
        self.__cantVertices=vertices
        self.__Matriz=np.zeros((vertices, vertices))
        
#b)
        
    def gradoEntrada(self, vertice):
        grado=0
        for i in range(self.__cantVertices):
            if self.__Matriz[i, vertice]>0:
                grado+=1
        return grado
    def gradoSalida(self, vertice):
        grado=0
        for i in range(self.__cantVertices):
            if self.__Matriz[vertice, i]>0:
                grado+=1
        return grado

    def fuente(self, vertice):
        return self.gradoEntrada(vertice)==0 and self.gradoSalida(vertice)>0
    
    def Fuentes(self):
        for i in range(self.__cantVertices):
            if self.fuente(i)==0:
                print(f"el vertice {i} es fuente")
#c) 
#O(n)=Lineal. T(n)=n+1

#Ejercicio 3 Tabla hash
#a)

import numpy as np
class TablaHash:
    __Tabla:np.array
    __dimension:int
    
    def __init__(self, claves=9000, factorCarga=0.7):
        self.__dimension=self.proximoPrimo(claves//factorCarga)
        self.__dimension=np.empty(self.__dimension, dtype=object)
#b)
    def hash(self, clave):
        return clave % self.__dimension

#c)
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

                
# ====================================================================================
# Recuperatorio Parcial 2
# ====================================================================================

#Ejericicio 1 Arbol binario de busqueda
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
            if arbol.getIzquierdo()!=None:
                grado+=1
            if arbol.getDerecho()!=None:
                grado+=1
        return grado
#c)
    #O(n)=constante T(n)=6
    
#Ejercicio 2 Grafo
#a)
import numpy as np
class Grafo:
    __matriz:np.array
    __cantVertices:int
    
    def __init__(self, vertices):
        self.__cantVertices=vertices
        self.__matriz=np.zeros((vertices, vertices))
        
#b)
    def camino(self, origen, destino):
        if not (0 <= origen < self.__cantVertices) or not (0 <= destino < self.__cantVertices):
            print("Origen o destino fuera de rango")
            return []

        if origen == destino:
            print(f"Camino de {origen} a {destino}: {origen}")
            return [origen]

        cola = Cola()
        visitado = [False] * self.__CantidadVertices
        padre = [-1] * self.__CantidadVertices

        cola.insertar(origen)
        visitado[origen] = True

        encontrado = False
        # iterar hasta que la cola quede vacía o encontremos el destino
        while not cola.vacia() and not encontrado:
            u = cola.suprimir()
            for v in range(self.__CantidadVertices):
                if self.__MatrizAdyacencia[u, v] == 1 and not visitado[v]:
                    visitado[v] = True
                    padre[v] = u
                    cola.insertar(v)
                    if v == destino:
                        encontrado = True
                        

        if not encontrado:
            print(f"No hay camino entre {origen} y {destino}")
            return []

        # reconstruir camino desde destino a origen
        camino = []
        v = destino
        while v != -1:
            camino.append(v)
            v = padre[v]
        camino.reverse()

        print(f"Camino más simple de {origen} a {destino}: {' -> '.join(map(str, camino))}")
        return camino

#Ejercicio 3 Tabla hash

#b)
class Nodo:
    __dato:int
    __siguiente:None
    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None
class Hashing:
    __tabla:np.array
    __dimension:int
    def __init__(self, claves, colisiones):
        self.__dimension=self.proximoPrimo(claves//colisiones)
        self.__tabla=np.empty(self.__dimension, dtype=object)
#a)
    def hash(self, clave):
        strclave=str(clave)
        extraccion=int(strclave[-3:])
        return extraccion % self.__cantVertices

#c)
    def insertar(self, clave):
        pos=self.hash(clave)
        aux=pos
        cabeza=self.__tabla[aux]
        bandera=False
        if cabeza==None:
            self.__tabla[aux]==Nodo(clave)
        else:
            actual=cabeza
            while actual!=None and bandera==False:
                if actual.getDato()==clave:
                    print("la clave ya se encuentra en la tabla")
                    bandera=True
                actual=actual.getSiguiente()
            if bandera==False:
                nuevo=Nodo(clave)
                nuevo.setSiguiente(cabeza)
                self.__tabla[pos]=nuevo
#d)
#O(n)=lineal T(n)=3(n+3)+9  

#====================================================================================
# extraordinario Parcial 2
# ====================================================================================
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
            if arbol.getIzquierdo()!=None:
                grado+=1
            if arbol.getDerecho()!=None:
                grado+=1
        return grado
            
    def NodosHoja(self, arbol):
        if arbol!=None:
            self.NodosHoja(arbol.getIzquierdo())
            if self.grado(arbol)==0:
                print(f"el nodo {arbol.getDato()} del arbol es un nodo Hoja")
            self.NodosHoja(arbol.getDerecho())
#c)
#O(n)=lineal. T(n)=2(n/2)

#Ejercicio 2 Digrafo
#a)
class Digrafoo:
    __matriz:np.array
    __cantVertices:int
    def __init__(self, vertices):
        self.__cantVertices=vertices
        self.__matriz=np.zeros((vertices,vertices))
    
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
    
    def fuente(self, vertice):
        return self.gradoEntrada(vertice)==0 and self.gradoSalida(vertice)>0
    
    def verticesFuente(self):
        for i in range(self.__cantVertices):
            if self.fuente(i):
                print(f'el vertice {i} es fuente')
#c)
#O(n)=lineal T(n)=n+1

#Ejercicio 3 Tabla Hash
#b)
class Hash:
    __Tabla:np.array
    __dimension:int
    def __init__(self, claves=5000, factorCarga=0.7):
        self.__dimension=self.proximoPrimo(claves//factorCarga)
        self.__Tabla=np.empty(self.__dimension, dtype=object)

#a)
    def hash(self, clave):
        pos=clave*clave
        strpos=str(pos)
        cuadradoMedio=int(strpos[3:])
        return cuadradoMedio%self.__dimension
    
    def insertar(self, clave):
        pos =self.hash(clave)
        aux=pos
        bandera=False
        if self.__Tabla[aux]==None:
            self.__Tabla[aux]=clave
        elif self.__Tabla[aux]==clave:
            print('clave existente')
        else:
            aux=(aux+1)%self.__dimension
            while self.__Tabla[aux]!=None and aux!=pos and bandera==False:
                if self.__tabla[aux]==clave:
                    bandera=True
                aux=(aux+1)%self.__Tabla
            if aux==pos:
                print('tabla llena')
            elif bandera==True:
                print('la clave ya se encuentra en la tabla')
            else:
                self.__Tabla[aux]=clave
        
        

    
   
       
        
 
    