from pilaS import Pila
def convercion(elem):
    pila=Pila(50)
    while elem>=2:
        pila.insertar(elem%2)
        elem=elem//2
    pila.insertar(elem)      
    pila.recorrer()

if __name__=="__main__":
    convercion(11)