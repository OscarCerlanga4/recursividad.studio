#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe



def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    return n * factorial(n-1)
    
    
if __name__ == "__main__":
    
    x = 3
    print(factorial(x))
    
    x = 2
    print(factorial(x))
    
    x = 1
    print(factorial(x))