from figura import Figura
import math 

class Circulo(Figura):
    def __init__(self, radio, color= "negro"):
        super().__init__(color)
        self.radio = radio
        
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio
    
   