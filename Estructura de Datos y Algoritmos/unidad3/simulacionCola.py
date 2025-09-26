from colaS import Cola
import random

def simulacion(tiempo):
    tllegada = 2
    cajero = 0  # 0 = libre, >0 = ocupado con tiempo restante
    reloj = 0
    cont = 0
    acumularT = 0
    cola = Cola()
    while reloj < tiempo:
        n = random.uniform(0.0, 1.0)
        # Llega un cliente
        if 0 <= n <= (1 / tllegada):
            cola.insertar(reloj)
        # Si el cajero está libre y hay clientes, atiende a uno
        if cajero == 0 and not cola.vacia():
            cliente = cola.suprimir()
            tiempoEspera = reloj - cliente
            acumularT += tiempoEspera
            cont += 1
            cajero = 5  # tiempo de atención
        # Si el cajero está ocupado, descuenta tiempo
        if cajero > 0:
            cajero -= 1
        reloj += 1

    if cont > 0:
        print(f"El tiempo de espera promedio de los clientes atendidos es: {acumularT / cont}")
    else:
        print("No se atendió ningún cliente.")

    suma = 0
    cant = 0
    while not cola.vacia():
        client = cola.suprimir()
        suma += reloj - client
        cant += 1
    if cant > 0:
        print(f"El tiempo de espera promedio de los clientes no atendidos es: {suma / cant}")
    else:
        print("No quedaron clientes sin atender.")
    print(f"La cantidad de clientes no atendidos es: {cant}")

if __name__ == "__main__":
    simulacion(240)