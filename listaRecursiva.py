#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe


def imprime(lista):
    
    print("<", end="")
    if len(lista) == 0:
        print(">", end="")
        return
    primero = lista[0]
    ListaRestantes = lista [1:]
    print(primero, end = ", ")
    imprime(ListaRestantes) 
    
    
    
if __name__ == "__main__":
    
    l = [33,22,11]
    imprime(l)
    
    #l = [33,22]
    #imprime(l)
    
    #l = [33]
    #imprime(l)
    
    #l = []
    #imprime(l)
    
    