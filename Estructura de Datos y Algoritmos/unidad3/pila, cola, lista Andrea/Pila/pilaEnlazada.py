class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaEncadenada:
    def __init__(self):
        self.tope = None

    def Vacia(self):
        return self.tope is None

    def Insertar(self, elemento):
        nuevo = Nodo(elemento)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def Suprimir(self):
        if self.Vacia():
            print("La pila está vacía")
        else:
            self.tope = self.tope.siguiente

    def RecuperarTope(self):
        if self.Vacia():
            print("La pila está vacía")
        else:
            return self.tope.dato
        
    def Recorrer(self):
        actual = self.tope
        while actual:
            print(actual.dato)
            actual = actual.siguiente

if __name__ == "__main__":
    p = PilaEncadenada()
    p.Insertar(1)
    p.Insertar(2)
    p.Insertar(3)
    p.Insertar(4)
    p.Insertar(5)
    p.Recorrer()