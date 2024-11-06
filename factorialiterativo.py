#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe



def factorial(n):
    fact = 1
    actual = n
    while actual > 0:
        fact = fact * actual
        actual = actual - 1
    return fact
    
    
if __name__ == "__main__":
    
    x = 3
    print(factorial(x))
    
    x = 2
    print(factorial(x))
    
    x = 1
    print(factorial(x))