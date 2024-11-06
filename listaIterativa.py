#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe




def imprime(lista):
    """impresion iterativa de una lista
    con enfoque primero+restantes"""
    print("( ", end="")
    if len(lista) == 0:
        print(")", end="")
        return
    
    print(lista[0], end=" ")
    
    imprime(lista[1:])
    
    print("( ", end="")

 
if __name__ == "__main__":
    
    l = [33,22,11]
    imprime(l)
    print()    
    
    l = [33,22]
    imprime(l)
    print()
    
    l = [33]
    imprime(l)
    print()
    
    l = []
    imprime(l)
    print()
    
    