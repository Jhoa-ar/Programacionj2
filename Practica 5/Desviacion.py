import math

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros 
    def promedio(self):
        return sum(self.numeros) / len(self.numeros)
    def desviacion(self):
        m = self.promedio()
        suma = sum((x - m) ** 2 for x in self.numeros)
        return math.sqrt(suma / (len(self.numeros) - 1 ))
    
numeros = list(map(float, input("ingrese 10 numeros: ").split()))

if len(numeros) != 10:
    print("ingrese 10 numeros")
else:
    estadisticas = Estadistica(numeros)
    m = estadisticas.promedio()
    Desviacion = estadisticas.desviacion()
    
    print(f"El promedio es {m}")
    print(f"La desviacion estandar es {Desviacion}")