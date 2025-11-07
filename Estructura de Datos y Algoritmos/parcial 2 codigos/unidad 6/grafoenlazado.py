
import numpy as np
## ============================
# Clase Pila
# ============================
class Pila:
    __tope:int
    __datos:np.array
    def __init__(self, capacidad=100):
        self.__tope = -1
        self.__datos = np.empty(capacidad, dtype=object)
    
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, elemento):
        self.__tope += 1
        self.__datos[self.__tope] = elemento
    
    def suprimir(self):
        if not self.vacia():
            elemento = self.__datos[self.__tope]
            self.__tope -= 1
            return elemento
        return None

# ============================
# Clase Cola
# ============================
class Cola:
    __datos:np.array
    __primero:int
    __ultimo:int
    __cantidad:int
    __tamaño:int
    def __init__(self, tamaño=100):
        self.__datos = np.empty(tamaño, dtype=object)
        self.__primero = 0
        self.__ultimo = -1
        self.__tamaño = tamaño
        self.__cantidad =0
    
    def vacia(self):
        return self.__cantidad== 0
    
    def insertar(self, elemento):
        if self.__cantidad < self.__tamaño:
            self.__ultimo = (self.__ultimo + 1) % self.__tamaño
            self.__datos[self.__ultimo] = elemento
            self.__cantidad += 1
    
    def suprimir(self):
        if not self.vacia():
            elemento = self.__datos[self.__primero]
            self.__primero = (self.__primero + 1) % self.__tamaño
            self.__cantidad -= 1
            return elemento
        return None

# ============================
# Clase GrafoLista ponderado
# ============================
class NodoAdyacente:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso
        self.sig = None
        
class GrafoLista:
    def __init__(self, vertices, nombres):
        self.__vertices = vertices
        self.__nombres = nombres
        self.__listas = np.array([None] * vertices)

    def insertar_arista(self, origen, destino, peso):
        nodo = NodoAdyacente(destino, peso)
        nodo.sig = self.__listas[origen]
        self.__listas[origen] = nodo

        nodo2 = NodoAdyacente(origen, peso)  # grafo no dirigido
        nodo2.sig = self.__listas[destino]
        self.__listas[destino] = nodo2
    def adyacentes(self, v):
        if v<0 and v<self.__vertices:
            print("El vertice ingresado no existe")
        else:
         print("adyacentes a ", self.__nombres[v])    
         ady=self.__listas[v]
         while ady:
          print(f" -> {self.__nombres[ady.destino]} ({ady.peso} km)", end="")
          ady = ady.sig
          print()
    def grado(self,v): 
        if v<0 and v<self.__vertices:
            print("El vertice ingresado no existe")
        else:
         grado=0   
         ady=self.__listas[v]
         while ady:
           grado+=1
           ady = ady.sig
         print("El grado del vertice ", self.__nombres[v], "es ", grado )
 
    def mostrar(self):
        print("LISTA DE ADYACENCIA (ponderada):")
        for i in range(self.__vertices):
            print(f"{self.__nombres[i]}:", end=" ")
            ady = self.__listas[i]
            while ady:
                print(f" -> {self.__nombres[ady.destino]} ({ady.peso} km)", end="")
                ady = ady.sig
            print()
  # ============================
    # Camino simple entre dos vértices
    # ============================
    def camino(self, origen, destino):
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
                print(self.__nombres[i], end=" -> ")
            print("FIN")
        else:
            print("\nNo existe camino entre los vértices indicados.")
    # ============================
    # Búsqueda en profundidad (DFS)
    # ============================
    def BEP(self, inicio):
        print("\nRECORRIDO EN PROFUNDIDAD (DFS):")
        visitado = [False] * self.__vertices
        pila = Pila()
        pila.insertar(inicio)

        while not pila.vacia():
            v = pila.suprimir()
            if not visitado[v]:
                print(self.__nombres[v])
                visitado[v] = True
                ady = self.__listas[v]
                while ady:
                    if not visitado[ady.destino]:
                        pila.insertar(ady.destino)
                    ady = ady.sig

    # ============================
    # Búsqueda en anchura (BFS)
    # con distancias y predecesores
    # ============================
    def BEA(self, inicio, destino=None):
        print("\nRECORRIDO EN ANCHURA (BFS):")
        visitado = [False] * self.__vertices
        distancia = [np.inf] * self.__vertices
        predecesor = [-1] * self.__vertices

        cola = Cola(self.__vertices)
        cola.insertar(inicio)
        visitado[inicio] = True
        distancia[inicio] = 0

        while not cola.vacia():
            v = cola.suprimir()
            print(self.__nombres[v])

            ady = self.__listas[v]
            while ady:
                if not visitado[ady.destino]:
                    cola.insertar(ady.destino)
                    visitado[ady.destino] = True
                    distancia[ady.destino] = distancia[v] + 1
                    predecesor[ady.destino] = v
                ady = ady.sig

        print("\nDistancia (en número de aristas) desde", self.__nombres[inicio], ":")
        for i in range(self.__vertices):
            d = "∞" if distancia[i] == np.inf else int(distancia[i])
            print(f"  {self.__nombres[i]}: {d}")

        # Si se pide un destino, mostramos los caminos
        if destino is not None:
            print(f"\nTodos los caminos posibles desde {self.__nombres[inicio]} hasta {self.__nombres[destino]}:")
            self.__mostrar_todos_caminos(inicio, destino)

        return distancia, predecesor

    # ============================
    # Mostrar todos los caminos entre dos vértices
    # ============================
    def mostrar_todos_caminos(self, origen, destino):
        visitado = [False] * self.__vertices
        camino = []
        distancia=0

        def BEP_caminos(v,distancia):
            visitado[v] = True
            distancia+=self.__listas[v].peso
            camino.append(v)
            if v == destino:
                print(" -> ".join(self.__nombres[i] for i in camino))
                print("Distancia ", distancia)
            else:
                ady = self.__listas[v]
                while ady:
                    if not visitado[ady.destino]:
                        BEP_caminos(ady.destino,distancia)
                    ady = ady.sig
            camino.pop()
            visitado[v] = False

        BEP_caminos(origen, distancia)
        
    def conexo(self):
        visitado = [False] * len(self.__nombres)
        self.BEA(0)  # Comienza la búsqueda desde el nodo 0

        # Verifica si todos los nodos han sido visitados
        return all(visitado)
       

    # ============================
    # Dijkstra
    # ============================
    def dijkstra(self, origen):
        dist = [np.inf] * self.__vertices
        visitado = [False] * self.__vertices
        dist[origen] = 0

        for _ in range(self.__vertices):
            min_dist = np.inf
            u = -1
            for i in range(self.__vertices):
                if not visitado[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            if u == -1:
                break

            visitado[u] = True
            ady = self.__listas[u]
            while ady:
                if not visitado[ady.destino] and dist[u] + ady.peso < dist[ady.destino]:
                    dist[ady.destino] = dist[u] + ady.peso
                ady = ady.sig

        print(f"\nDistancias mínimas desde {self.__nombres[origen]}:")
        for i in range(self.__vertices):
            valor = "∞" if dist[i] == np.inf else int(dist[i])
            print(f"  {self.__nombres[i]}: {valor} km")
     
 
# ============================
# PROGRAMA PRINCIPAL
# ============================
if __name__ == "__main__":
    provincias = [
    "Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "San Luis",
    "San Juan", "La Pampa", "Neuquén", "Río Negro", "Chubut"
    ]

    g = GrafoLista(len(provincias), provincias)

# Aristas (no dirigidas)
    g.insertar_arista(0, 1, 710)
    g.insertar_arista(0, 2, 475)
    g.insertar_arista(1, 3, 620)
    g.insertar_arista(1, 4, 420)
    g.insertar_arista(2, 6, 580)
    g.insertar_arista(3, 5, 160)
    g.insertar_arista(4, 6, 500)
    g.insertar_arista(6, 7, 740)
    g.insertar_arista(7, 8, 450)
    g.insertar_arista(8, 9, 580)
#g.caminos_y_mas_corto(0,5)
    origen = 0   # Buenos Aires
    destino = 5  # San Juan
    print("==================================================================")
    print(f"\nTodos los caminos posibles desde {provincias[origen]} hasta {provincias[destino]} con sus pesos:")
    g.mostrar_todos_caminos(0,5)
    print("==================================================================")
    g.grado(1)
    print("==================================================================")
    g.mostrar()
# DFS
    print("==================================================================")
    g.BEP(0)
# BF 
    print("==================================================================")
    g.BEA(0)

# Conexo
    if g.conexo():
     print("\nEl grafo es CONEXO")
    else:
     print("\nEl grafo NO es conexo")

# Camino simple
    print("==================================================================")
    g.camino(0, 5)

# Dijkstra
    print("==================================================================")
    g.dijkstra(0)

# Floyd–Warshall
#g.warshall()
    print("==================================================================") 
    g.adyacentes(1)
    print()
    

   #print()
    #print(todos)
 # """ total=0
 #   for camino in todos:
 #     total+=camino.peso  
 #     print(" -> ".join(camino), f"| Total: {total} km")
      

   # if mas_corto:
   #    print("\nCamino más corto:")
   #    print(" -> ".join(mas_corto[0]), f"| Total: {mas_corto[1]} km")
   # else:
   #    print("\nNo existe ningún camino entre estos nodos.")

# Búsqueda en anchura (con caminos)"""


#
