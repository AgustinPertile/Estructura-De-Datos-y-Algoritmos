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
        if Arbol is None:
            print ("El nodo no existe en el arbol")
        if elemento > Arbol.getDato():
            self.Hoja(Arbol.getDerecho(), elemento)
        elif elemento < Arbol.getDato():
            self.Hoja(Arbol.getIzquierdo(), elemento)
        else:
            if self.Grado(Arbol) == 0:
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
        if Arbol == None:
            print ("Arbol vacio")
        elif elemento < Arbol.getDato():
            Arbol.setIzquierdo(self.Suprimir(Arbol.getIzquierdo(), elemento))
        elif elemento > Arbol.getDato():
            Arbol.setDerecho(self.Suprimir(Arbol.getDerecho(), elemento))
        else:
            if self.Grado(Arbol) == None:
                return None
            if Arbol.getIzquierdo () is None:
                return Arbol.getDerecho()
            if Arbol.getDerecho() is None:
                return Arbol.getIzquierdo()
            
            sucesor = Arbol.getDerecho()
            while sucesor.getIzquierdo() is not None:
                sucesor = sucesor.getIzquierdo()
            Arbol.setDato(sucesor.getDato())
            Arbol.setDerecho(self.Suprimir(Arbol.getDerecho(), sucesor.getDato()))
        return Arbol
    
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
        if Arbol is None:
            print ("El nodo no existe en el arbol")
        if elemento > Arbol.getDato():
            self.Hoja(Arbol.getDerecho(), elemento)
        elif elemento < Arbol.getDato():
            self.Hoja(Arbol.getIzquierdo(), elemento)
        else:
            pass
    
    
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
    