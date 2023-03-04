def fibonacci(n):
    if n<=1:
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    #55514
    
numero = int (input("Ingresa el rango"))
for i in range(numero): 
    print(fibonacci(i)) 
        
