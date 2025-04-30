from figura import Figura
from colorear  import Coloreado

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="verde"):
        super().__init__(color)
        self.lado = lado
        
    def area(self):
        return self.lado ** 2 
    
    def perimetro(self):
        return 4 * self.lado
    
    def comoColorear(self):
        return "Colorear los cuatro lados"
    
    
    