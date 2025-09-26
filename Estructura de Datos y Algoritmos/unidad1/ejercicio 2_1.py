def producto():
    m=0
    cont=0
    n=int(input("ingrese un numero: "))
    m=n*n
    cont += 1
    print(f"resultado: {m} \n Contador: {cont} ")
    
    
def suma():
    n=int(input("ingrese un numero: "))
    cont=0
    m=0
    for i in range(n):
        m=m+n
        cont += 1
    print(f"resultado: {m} \n Contador: {cont} ")
    
def incremento():
    n=int(input("ingrese un numero: "))
    cont=0
    m=0
    for i in range(n):
        for j in range(n):
           m=m+1
           cont += 1
    print(f"resultado: {m} \n Contador: {cont} ")
    
suma()
producto()
incremento()
            