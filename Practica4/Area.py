from multimethod import multimethod
import math

class FigurasGeometricas:
    
    @multimethod
    def area(self, r: float):  
        return math.pi * r**2
    
    @multimethod
    def area(self, b: int, h: int):
        return b * h
     
    @multimethod
    def area(self, b: float, h: float):
        return (b * h)/2
    
    @multimethod
    def area(self, B: float, b: float, h: float):
        return ((B + b) * h) / 2 
    
    @multimethod
    def area(self, L: float, a: float):
        P = 5 * L
        return (P * a)/2
    
figura = FigurasGeometricas()

print("Área del círculo:", figura.area(5.0))                
print("Área del rectángulo:", figura.area(10, 4))          
print("Área del triángulo rectángulo:", figura.area(8.0, 6.0))  
print("Área del trapecio:", figura.area(10.0, 6.0, 5.0))  
print("Área del Pentagono:", figura.area(7.0, 4.0))