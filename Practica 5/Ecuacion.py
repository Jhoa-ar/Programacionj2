import math 
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c 
    
    def getDiscriminante(self):
        return self.b**2 - 4*self.a*self.c
    def getRaiz1(self):
        discriminante = self.getDiscriminante()
        if discriminante >= 0:
            return (- self.b - math.sqrt(discriminante)) / (2 * a)
        return None
    def getRaiz2(self):
        discriminante = self.getDiscriminante()
        if discriminante > 0:
            return (- self.b - math.sqrt(discriminante)) / (2 * a)
        return None
    
    def Resolver(self):
        discriminante = self.getDiscriminante()
       
        if discriminante > 0:
           print (f"Las raices de la ecuacion son: {self.getRaiz1()}, {self.getRaiz2()}")
        elif discriminante == 0:
            print (f"La ecuacion solo tiene una raiz es: {self.getRaiz1()}")    
        else:
            print (f"La ecuacion no tiene raıces reales")

a = float(input("ingrese a: "))
b = float(input("ingrese b: "))
c = float(input("ingrese c: "))

ecuacion = EcuacionCuadratica(a, b, c)
ecuacion.Resolver()