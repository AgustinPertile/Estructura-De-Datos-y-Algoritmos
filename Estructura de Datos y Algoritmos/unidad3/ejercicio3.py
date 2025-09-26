from pilaS import Pila

'''def subirEscalera(n):
    pila = Pila(50)  # Capacidad suficiente para los estados
    secuencias = []     # Lista paralela para las secuencias de pasos

    # Estado inicial: suma=0, secuencia vacía
    pila.insertar(0)
    secuencias.append([])

    while not pila.vacia():
        suma_actual = pila.suprimir()
        secuencia_actual = secuencias.pop()

        if suma_actual == n:
            print(secuencia_actual)
        elif suma_actual < n:
            for paso in range(1, n + 1):
                if suma_actual + paso <= n:
                    pila.insertar(suma_actual + paso)
                    secuencias.append(secuencia_actual + [paso])'''

def subirEscalera(n):
    pila=Pila(50)
    secuencias=[]
    while n>0:
        if n%2==0:
            secuencias.append(2)
    pass

if __name__ == "__main__":
    subirEscalera(7)