from pilaS import Pila
from colaS import Cola
import numpy as np
class NodoAdyacente:
    def __init__(self, destino):
        # usar atributos no mangled para compatibilidad con el resto del código
        self.destino = destino
        self.sig = None

    def getDestino(self):
        return self.destino

    def getSiguiente(self):
        return self.sig
        
class DigrafoEnlazado:
    def __init__(self, vertices):
        self.__vertices = vertices
        self.__listas = np.array([None] * vertices)

    def insertar_arista(self, origen, destino):
            nodo = NodoAdyacente(destino)
            nodo.sig = self.__listas[origen]
            self.__listas[origen] = nodo
    
    def adyacentes(self, vertice):
        adyacentes = []
        if 0 <= vertice < self.__vertices:
            actual = self.__listas[vertice]
            while actual is not None:
                adyacentes.append(actual.getDestino())
                actual = actual.getSiguiente()
            print(f"adyacentes al vertice {vertice}: {adyacentes}")

    def gradoSalida(self, vertice):
        grado=0
        if 0 <= vertice < self.__vertices:
            actual = self.__listas[vertice]
            while actual is not None:
                grado+=1
                actual = actual.getSiguiente()
        return grado
    
    def gradoEntrada(self, vertice):
        grado=0
        for i in range(self.__vertices):
            actual = self.__listas[i]
            while actual is not None:
                if actual.getDestino()==vertice:
                    grado+=1
                actual = actual.getSiguiente()
        return grado
    
    def fuente(self, vertice):
        return self.gradoEntrada(vertice) == 0 and self.gradoSalida(vertice) > 0
    
    def sumidero(self, vertice):
        return self.gradoSalida(vertice) == 0 and self.gradoEntrada(vertice) > 0
            
    def fuenteYsumidero(self):
        fuente=[]
        sumidero=[]
        for i in range(self.__vertices):
            if self.fuente(i):
                fuente.append(i)
            else:
                if self.sumidero(i):
                    sumidero.append(i)
        print (f"El vertice {fuente} es fuente")
        print (f"El vertice {sumidero} es sumidero")
        return fuente, sumidero
    
    def BEP(self, inicio):
        print("\nRECORRIDO EN PROFUNDIDAD (DFS):")
        visitado = [False] * self.__vertices
        pila = Pila()
        pila.insertar(inicio)

        while not pila.vacia():
            v = pila.suprimir()
            if not visitado[v]:
                print(v)
                visitado[v] = True
                ady = self.__listas[v]
                while ady:
                    if not visitado[ady.destino]:
                        pila.insertar(ady.destino)
                    ady = ady.sig
                    break
    
    
    def BEA(self, inicio, destino=None):
        print("\nRECORRIDO EN ANCHURA (BFS):")
        visitado = [False] * self.__vertices
    
        cola = Cola(self.__vertices)
        cola.insertar(inicio)
        visitado[inicio] = True
        

        while not cola.vacia():
            v = cola.suprimir()
            print(v)

            ady = self.__listas[v]
            while ady:
                if not visitado[ady.destino]:
                    cola.insertar(ady.destino)
                    visitado[ady.destino] = True
                ady = ady.sig
        return visitado
                
    def conexo(self):
        # Reutiliza BEA para obtener el array de visitados
        visitado = self.BEA(0)
        return all(visitado)
    
    def camino(self, origen, destino):
        # Validación de índices
        if not (0 <= origen < self.__vertices and 0 <= destino < self.__vertices):
            print(f"\nÍndices fuera de rango")
        else:
            visitado = [False] * self.__vertices
            camino = []

            def buscar(v):
                visitado[v] = True
                camino.append(v)
                if v == destino:
                    return True
                ady = self.__listas[v]
                while ady:
                    if not visitado[ady.destino]:
                        if buscar(ady.destino):
                            return True
                    ady = ady.sig
                camino.pop()
                return False

            if buscar(origen):
                print("\nCamino encontrado:")
                for i in camino:
                    print(i, end=" -> ")
                print("FIN")
            else:
                print("\nNo existe camino entre los vértices indicados.")
                
    def aciclico(self):
        # Usamos DFS con coloreado: 0 = no visitado, 1 = en pila (visiting), 2 = procesado
        estado = [0] * self.__vertices

        def dfs(u):
            estado[u] = 1
            ady = self.__listas[u]
            while ady:
                v = ady.destino
                if estado[v] == 1:
                    # arista a un vértice en proceso -> ciclo
                    return True
                if estado[v] == 0:
                    if dfs(v):
                        return True
                ady = ady.sig
            estado[u] = 2
            return False

        for i in range(self.__vertices):
            if estado[i] == 0:
                if dfs(i):
                    print("\nEl grafo tiene ciclos (NO es acíclico)")
                    return False
        print("\nEl grafo es ACÍCLICO")
        return True
            
    def mostrar(self):
       for i in range(self.__vertices):
            actual = self.__listas[i]
            if actual is None:
                print(f"[{i}]: -")
            else:
                elems = []
                while actual is not None:
                    elems.append(str(actual.getDestino()))
                    actual = actual.getSiguiente()
                print (f"[{i}]: " + " -> ".join(elems))
    
    
            
if __name__=="__main__":
    g=DigrafoEnlazado(5)
    g.insertar_arista(0,0)
    g.insertar_arista(0,1)
    g.insertar_arista(0,2)
    g.insertar_arista(2,4)
    g.insertar_arista(4,3)
    g.insertar_arista(3,3)
    g.insertar_arista(3,1)
    g.insertar_arista(2, 3)
    g.insertar_arista(4,2)
    g.insertar_arista(1,2)
    g.insertar_arista(1,3)
    g.insertar_arista(1,4)
    g.insertar_arista(2,0)
    g.mostrar()
    g.adyacentes(0)
    print("Grado de salida de 0:", g.gradoSalida(0))
    print("Grado de entrada de 0:", g.gradoEntrada(0))
    for i in range(5):
        print(g.fuente(i))
        print(g.sumidero(i))
    g.fuenteYsumidero()
    g.BEP(0)
    g.BEA(0)
    if g.conexo():
     print("\nEl grafo es CONEXO")
    else:
     print("\nEl grafo NO es conexo")
    g.camino(1,4)
    g.aciclico()