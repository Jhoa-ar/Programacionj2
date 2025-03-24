import math 

def promedio(numeros):
    return sum(numeros)/ len(numeros)
def desviacion(numeros):
    m = promedio(numeros)
    suma = sum((x - m) ** 2 for x in numeros)
    return math.sqrt(suma / (len(numeros) - 1))
numeros = list(map(float, input ("ingresa 10 numeros: ").split()))

if len(numeros) != 10:
    print("ingresar 10 numeros")
else:
    m = promedio(numeros)
    Desviacion = desviacion(numeros)
    
    print(f"El promedio es {m}")
    print(f"La desviacion estandar es {Desviacion}")