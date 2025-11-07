class Nodo ():
    __Dato:int
    __Izquierdo:None
    __Derecho:None
    
    def __init__(self, dato):
        self.__Dato = dato
        self.__Izquierdo = None
        self.__Derecho = None
        
    def getDato (self):
        return self.__Dato
    
    def setDato (self, num):
        self.__Dato = num

    def getIzquierdo (self):
        return self.__Izquierdo
    
    def setIzquierdo (self, num):
        self.__Izquierdo = num
    
    def getDerecho (self):
        return self.__Derecho
    
    def setDerecho (self, num):
        self.__Derecho = num
        
class Arbol ():
    __Raiz: Nodo
    
    def __init__(self):
        self.__Raiz = None 
    
    def getRaiz(self):
        return self.__Raiz
    
    def setRaiz(self, num):
        self.__Raiz = num
        
        
    def Grado (self, Arbol):
        grado=0
        if Arbol.getIzquierdo() is not None:
            grado += 1
        if Arbol.getDerecho() is not None:
            grado += 1
        return grado
    
    
    def Hoja (self, Arbol, elemento):
        # Busca el elemento y determina si es hoja
        nodo = self._buscar_nodo(self.__Raiz, elemento)
        if nodo is None:
            print("El nodo no existe en el arbol")
        if self.Grado(nodo) == 0:
            print("El nodo es hoja")
        else:
            print("El nodo no es hoja")
            
    
    
    #Para insertar se entra siempre por la raiz 
    
    def Insertar (self, aux, num):
        nuevo = Nodo(num)
        if self.__Raiz is None:
            self.setRaiz(nuevo)
        else:
            if nuevo.getDato() > aux.getDato():
                if aux.getDerecho() is None:
                    aux.setDerecho(nuevo)
                else:    
                    self.Insertar(aux.getDerecho(), num)
            if nuevo.getDato() < aux.getDato():
                if aux.getIzquierdo() is None:
                    aux.setIzquierdo(nuevo)
                else:
                    self.Insertar(aux.getIzquierdo(), num)
            
            
    def Suprimir (self, Arbol, elemento):
        # Suprimir devuelve la nueva subraíz después de borrar el elemento.
        nuevo = Arbol
        if Arbol is None:
            nuevo = None
        else:
            if elemento < Arbol.getDato():
                Arbol.setIzquierdo(self.Suprimir(Arbol.getIzquierdo(), elemento))
            elif elemento > Arbol.getDato():
                Arbol.setDerecho(self.Suprimir(Arbol.getDerecho(), elemento))
            else:
                # caso con 0 o 1 hijo
                if Arbol.getIzquierdo() is None:
                    nuevo = Arbol.getDerecho()
                elif Arbol.getDerecho() is None:
                    nuevo = Arbol.getIzquierdo()
                else:
                    # caso 2 hijos: usar sucesor (mínimo en subárbol derecho)
                    sucesor = Arbol.getDerecho()
                    while sucesor.getIzquierdo() is not None:
                        sucesor = sucesor.getIzquierdo()
                    Arbol.setDato(sucesor.getDato())
                    Arbol.setDerecho(self.Suprimir(Arbol.getDerecho(), sucesor.getDato()))
        return nuevo
    
    
    def RecorrerInorden (self, arbol):
        if arbol != None:
            self.RecorrerInorden(arbol.getIzquierdo())
            print (f"{arbol.getDato()}")
            self.RecorrerInorden(arbol.getDerecho())
            
            
    def RecorrerPreorden (self, arbol):
        if arbol != None:
            print (f"{arbol.getDato()}")
            self.RecorrerPreorden(arbol.getIzquierdo())
            self.RecorrerPreorden(arbol.getDerecho())
            
            
    def RecorrerPostorden (self, arbol):
        if arbol != None:
            self.RecorrerPostorden(arbol.getIzquierdo())
            self.RecorrerPostorden(arbol.getDerecho())
            print (f"{arbol.getDato()}")
        
        
    def Buscar (self, Arbol, elemento):
        # Buscar devuelve el Nodo con el dato (o None). Implementación pública.
        nodo = self._buscar_nodo(Arbol, elemento)
        if nodo is None:
            print("El nodo no existe en el arbol")
        else:
            print(f"Nodo encontrado: {nodo.getDato()}")
        return None


    def _buscar_nodo(self, arbol, elemento):
        if arbol is None:
            return None
        if elemento == arbol.getDato():
            return arbol
        if elemento < arbol.getDato():
            return self._buscar_nodo(arbol.getIzquierdo(), elemento)
        else:
            return self._buscar_nodo(arbol.getDerecho(), elemento)


    def Nivel(self, elemento):
        """Imprime el nivel (profundidad) del elemento en el árbol (raíz nivel 0)."""
        nivel = 0
        nodo = self.__Raiz
        while nodo is not None:
            if elemento == nodo.getDato():
                print(f"Nivel de {elemento}: {nivel}")
                # mostrar en vez de devolver
                return None
            elif elemento < nodo.getDato():
                nodo = nodo.getIzquierdo()
            else:
                nodo = nodo.getDerecho()
            nivel += 1
        print("El nodo no existe en el arbol")
        return None
    
    
    def unDescendiente (self, arbol):
        cont=0
        if arbol != None:
            if self.grado(arbol)==1:
                print(f"{arbol.getDato()}")
                cont+=1
            cont+=self.unDescendiente(arbol.getIzquierdo())
            cont+=self.unDescendiente(arbol.getDerecho())
        return cont
    
    
    def Padre(self, elemento):
        """Imprime el padre del elemento si existe."""
        padre = None
        nodo = self.__Raiz
        while nodo is not None and nodo.getDato() != elemento:
            padre = nodo
            if elemento < nodo.getDato():
                nodo = nodo.getIzquierdo()
            else:
                nodo = nodo.getDerecho()
        if nodo is None:
            print("El nodo no existe en el arbol")
            return None
        if padre is None:
            print(f"El nodo {elemento} es la raiz y no tiene padre")
            return None
        print(f"Padre de {elemento}: {padre.getDato()}")
        # mostrar en vez de devolver
        return None


    def Hijo(self, elemento):
        """Imprime los hijos (izquierdo/derecho) del nodo con valor 'elemento'."""
        nodo = self._buscar_nodo(self.__Raiz, elemento)
        if nodo is None:
            print("El nodo no existe en el arbol")
            return
        hijos = []
        if nodo.getIzquierdo() is not None:
            hijos.append(('izquierdo', nodo.getIzquierdo().getDato()))
        if nodo.getDerecho() is not None:
            hijos.append(('derecho', nodo.getDerecho().getDato()))
        if not hijos:
            print(f"El nodo {elemento} no tiene hijos")
        else:
            for pos, val in hijos:
                print(f"Hijo {pos} de {elemento}: {val}")
        return None


    def Camino(self, elemento):
        """Imprime el camino desde la raíz hasta el elemento (lista de valores)."""
        camino = []
        nodo = self.__Raiz
        while nodo is not None:
            camino.append(nodo.getDato())
            if elemento == nodo.getDato():
                print(f"Camino desde raiz hasta {elemento}: {camino}")
                return None
            elif elemento < nodo.getDato():
                nodo = nodo.getIzquierdo()
            else:
                nodo = nodo.getDerecho()
        print("El nodo no existe en el arbol")
        return None


    def Altura(self, arbol=None):
        """Devuelve e imprime la altura del árbol (número máximo de aristas raíz-hoja)."""
        if arbol is None:
            arbol = self.__Raiz
        def _altura(n):
            if n is None:
                return -1
            return 1 + max(_altura(n.getIzquierdo()), _altura(n.getDerecho()))
        h = _altura(arbol)
        print(f"Altura del arbol: {h}")
        return None


    def SuprimirValor(self, elemento):
        """Public wrapper: suprime 'elemento' en el árbol y muestra resultado en vez de devolverlo."""
        nodo = self._buscar_nodo(self.__Raiz, elemento)
        if nodo is None:
            print("Elemento a suprimir no existe en el arbol")
            return None
        self.__Raiz = self.Suprimir(self.__Raiz, elemento)
        print(f"Elemento {elemento} suprimido (si existía).")
        return None
    
    
if __name__ == "__main__":
    a = Arbol()
    a.Insertar (a.getRaiz(), 10)
    a.Insertar (a.getRaiz(), 5)
    a.Insertar (a.getRaiz(), 15)
    a.Insertar (a.getRaiz(), 3)
    a.Insertar (a.getRaiz(), 7)
    print ("-----------Inorden------------")
    a.RecorrerInorden (a.getRaiz())
    '''print ("-----------Preorden------------")
    a.RecorrerPreorden (a.getRaiz())
    print ("-----------Postorden------------")
    a.RecorrerPostorden (a.getRaiz())
    a.Suprimir(a.getRaiz(), 5)'''
    print ("---------------------------------------")
    a.RecorrerInorden (a.getRaiz())
    a.Hoja (a.getRaiz(), 7)
    