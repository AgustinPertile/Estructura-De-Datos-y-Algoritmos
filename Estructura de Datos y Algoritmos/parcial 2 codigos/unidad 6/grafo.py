import numpy as np
from colaS import Cola
from pilaS import Pila
class Grafo:
    __CantidadVertices:int
    __MatrizAdyacencia:np.array
    
    def __init__ (self, cant=5):
        self.__CantidadVertices = cant
        self.__MatrizAdyacencia = np.full ((cant, cant), 0)
        
    def Relaciones (self, origen, destino):
        if 0 <= origen <= self.__CantidadVertices and 0 <= destino <= self.__CantidadVertices:
            self.__MatrizAdyacencia [origen, destino] = 1
            self.__MatrizAdyacencia [destino, origen] = 1
        else:
            print ("Indices fuera de rango")
        
    def Mostrar (self):
        print (f"{self.__MatrizAdyacencia}")
        
    def Adyacentes (self, vertice):
        vertice -=1
        if 0 <= vertice <= self.__CantidadVertices:
            for j in range(len(self.__MatrizAdyacencia)):
                if self.__MatrizAdyacencia [vertice, j] == 1:
                    print (f"El vertice {vertice+1} es adyacente con el vertice {j+1}")
                    
    def busqueda_anchura (self, inicio):
        cola = Cola()
        visitados = set()
        recorrido = []

        cola.insertar(inicio)
        visitados.add(inicio)

        while not cola.vacia():
            actual = cola.suprimir()
            recorrido.append(actual)

            # recorrer vecinos usando la matriz de adyacencia
            for vecino in range(self.__CantidadVertices):
                if self.__MatrizAdyacencia[actual, vecino] == 1 and vecino not in visitados:
                    cola.insertar(vecino)
                    visitados.add(vecino)

        return recorrido
    
    def busqueda_profundidad(self, inicio):
        pila = Pila()
        visitados = set()
        recorrido = []

        pila.insertar(inicio)
        visitados.add(inicio)

        while not pila.vacia():
            actual = pila.suprimir()
            recorrido.append(actual)

            # recorrer vecinos en orden inverso para mantener un orden determinista similar al ejemplo
            for vecino in range(self.__CantidadVertices - 1, -1, -1):
                if self.__MatrizAdyacencia[actual, vecino] == 1 and vecino not in visitados:
                    pila.insertar(vecino)
                    visitados.add(vecino)

        return recorrido

    def Grado (self, vertice):
        grado=0
        for i in range(self.__CantidadVertices):
            if self.__MatrizAdyacencia[vertice, i] > 0:
                grado += 1
        return grado
    
    def Camino (self, origen, destino):
        caminos = []
        visitado = [False] * self.__CantidadVertices
        camino = []

        def busqueda_profundidad(u):
            visitado[u] = True
            camino.append(u)

            if u == destino:
                # guardar copia del camino
                caminos.append(camino.copy())
            else:
                for v in range(self.__CantidadVertices):
                    if self.__MatrizAdyacencia[u, v] == 1 and not visitado[v]:
                        busqueda_profundidad(v)

            # backtrack
            camino.pop()
            visitado[u] = False

        # comprobaciones de índices
        if not (0 <= origen < self.__CantidadVertices) or not (0 <= destino < self.__CantidadVertices):
            print("Origen o destino fuera de rango")
            return []

        busqueda_profundidad(origen)

        if not caminos:
            print(f"No hay caminos de {origen} a {destino}")
        else:
            print(f"Caminos de {origen} a {destino}:")
            for p in caminos:
                print(" -> ".join(map(str, p)))

        return caminos

    def CaminoSimple(self, origen, destino):
        # validación de índices
        if not (0 <= origen < self.__CantidadVertices) or not (0 <= destino < self.__CantidadVertices):
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
                        # no usamos break; la condición del while evitará otra iteración

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
    

if __name__ == "__main__":
    g=Grafo()
    g.Relaciones(0,0)
    g.Relaciones(0,1)
    g.Relaciones(0,2)
    g.Relaciones(2,4)
    g.Relaciones(4,3)
    g.Relaciones(3,3)
    g.Relaciones(20,3)
    g.Mostrar()
    g.Adyacentes(3)
    # llamadas de ejemplo: ahora bfs y busqueda_profundidad aceptan solo el vértice de inicio
    recorrido_bfs = g.bfs(0)
    print("BFS:", recorrido_bfs)
    recorrido_dfs = g.busqueda_profundidad(0)
    print("DFS:", recorrido_dfs)