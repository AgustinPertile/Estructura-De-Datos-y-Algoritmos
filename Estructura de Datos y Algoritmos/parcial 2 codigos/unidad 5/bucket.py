import numpy as np

class Hash:
    __tabla:np.array
    __areaPrimaria:int
    __overflow:int
    __comienzoOverflow:int
    __arregloSecundario:np.array
    __colisiones:int
    
    def __init__(self, claves=20, colisiones=4):
        self.__colisiones=colisiones
        self.__areaPrimaria=(claves//colisiones)
        self.__overflow=(20*(claves//colisiones)//100)
        self.__comienzoOverflow=self.__areaPrimaria
        self.__tabla=np.full((self.__areaPrimaria+self.__overflow, colisiones), None)
        self.__arregloSecundario=np.zeros(self.__areaPrimaria+self.__overflow, dtype=int)
        
    def hash(self, clave):
        return clave % self.__areaPrimaria
    
    def insertar(self, clave):
        '''pos = self.hash(clave)
        # intentar insertar en el área primaria (fila 'pos')
        
        cols = self.__tabla.shape[1]#.shape[1] devuelve el número de columnas (n).
        
        for j in range(cols):
            if self.__tabla[pos, j] is None:
                # insertar en primaria y aumentar contador de colisiones para la cubeta
                self.__tabla[pos, j] = clave
                if 0 <= pos < len(self.__arregloSecundario):
                    self.__arregloSecundario[pos] += 1
                return
            if self.__tabla[pos, j] == clave:
                print(f"El elemento {clave} ya existe en la tabla (primaria)")
                return

        # si la fila primaria está llena, usar la zona de overflow
        
        filas = self.__tabla.shape[0]#.shape[0] devuelve el número de filas (m) de la tabla.
        
        # primaria está llena: solo usar overflow si el contador de colisiones alcanzó el máximo
        for r in range(self.__comienzoOverflow, filas):
            for j in range(cols):
                if self.__tabla[r, j] is None:
                    self.__tabla[r, j] = clave
                    return
                if self.__tabla[r, j] == clave:
                    print(f"El elemento {clave} ya existe en la tabla (overflow)")
                    return

        print("La tabla está llena, no hay espacio para insertar")'''
        
        pos=self.hash(clave)
        if self.__arregloSecundario[pos]<self.__colisiones:
            self.__tabla[pos, self.__arregloSecundario[pos]]=clave
            self.__arregloSecundario[pos]+=1
        else:
            aux=self.__comienzoOverflow
            bandera=False
            while aux<len(self.__tabla) and bandera==False:
                if self.__arregloSecundario[aux]<self.__colisiones:
                    self.__tabla[aux, self.__arregloSecundario[aux]]=clave
                    self.__arregloSecundario[aux]+=1
                    bandera=True
                aux+=1
            
                    
            
        
    def buscar(self, clave):
            pos=self.hash(clave)
            filas = self.__tabla.shape[0]
            cols = self.__tabla.shape[1]
            band1=False
            band2=False

            j = 0
            while j < cols and band1==False:
                if self.__tabla[pos, j] == clave:
                    print(f"La clave se encuentra en la fila {pos+1} columna {j+1} del area primaria")
                    band1=True
                j += 1

           
            r = self.__comienzoOverflow
            while r < filas and band2==False:
                j = 0
                while j < cols and band2==False:
                    if self.__tabla[r, j] == clave:
                        print(f"La clave se encuentra en la fila {r+1} columna {j+1} del area overflow")
                        band2=True
                    j += 1
                r += 1
            if band1==False and band2==False:
                print("La clave no se encuentra en la tabla")

        
        
        
    def mostrar(self):
        print(f"{self.__tabla}")
        print(f"{self.__areaPrimaria}")
        print(f"{self.__overflow}")
        print(f"{self.__arregloSecundario}")
        
if __name__=="__main__":
    t=Hash()
    for i in range(24):
        t.insertar(i)
    t.buscar(13)
    t.mostrar()
    