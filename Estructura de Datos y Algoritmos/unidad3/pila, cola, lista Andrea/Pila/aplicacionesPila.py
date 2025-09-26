from pilaSecuencial import Pila

def Ejercicio2 (self, num):
    while num >= 2:
        p.Insertar (num % 2)
        num = num // 2
    p.Insertar (num)
                
def Ejercicio3 (self, num):
    while num > 0:
        if (num % 2) == 0:
            num - 2
        
        

if __name__ == "__main__":
    p=Pila(50)
    #p.Insertar(1)
    #p.Insertar(2)
    #p.Insertar(3)
    #p.Insertar(4)
    #p.Insertar(5)
    #p.Suprimir()
    #p.Suprimir()
    #p.Recorrer()
    #p.Ejercicio2(4)
    p.Ejercicio3(7)
    p.Recorrer()