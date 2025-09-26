from colaSecuencial import Cola
import random

def Simulacion ():
    TiempoDeEspera=0
    reloj=0
    cajero=0
    cont=0
    clientes_llegaron=0
    numero= random.uniform(0.0, 1.0)
    #frecuencia_llegada=2
    while reloj < 240:  #tiempo de espera de los clientes sin atender 
        if numero >= 0 and numero <= 0.5:
            clientes_llegaron += 1
            c.Insertar(reloj)
            if cajero == 5:
                if not c.Vacia():
                    aux=c.Suprimir()
                    print (f"llego en el tiempo {aux}")
                    TiempoDeEspera += (reloj-aux)
                    cont += 1
                    print (" TiempoDeEspera ", TiempoDeEspera)
                    cajero = 0
                else:
                    print ("La cola esta vacia")
            else:
                cajero += 1
        reloj += 1  
        numero= random.uniform(0.0, 1.0)
    PromedioTiempoDeEspera = (TiempoDeEspera/cont)  
    print (f"{cont}")
    print (f"La cantidad total del clientes que llegaron fue de: {clientes_llegaron}")
    print (f"El tiempo promedio de espera de los clientes es: {PromedioTiempoDeEspera}")
    
         

                    
            
    


if __name__ == "__main__":
    c=Cola()
    #c.Insertar(1)
    #c.Insertar(2)
    #c.Insertar(3)
    #c.Insertar(4)
    #c.Insertar(5)
    #c.Recorrer()
    #c.Suprimir()
    #c.Suprimir()
    Simulacion()
    #c.Recorrer()