from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color : str):
        self.color = color
        
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
    
    def __str__(self):
        return f"Color: {self.color}"
    @abstractmethod
    def area(self):
        pass
    
    def perimetro(self):
        pass