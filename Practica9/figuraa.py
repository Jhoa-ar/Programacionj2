import random
from abc import ABC, abstractmethod

class Coloreado:
    def comoColorear(self):
        pass

class Figura(ABC):
    def __init__(self, color="Rojo"):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="Rojo"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

class Circulo(Figura):
    def __init__(self, radio, color="Rojo"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

def main():
    for i in range(5):
        clase = random.choice([Cuadrado, Circulo])
        valor = random.randint(1, 10)  
        figura = clase(valor)  

        
        print(f"\nFigura {i+1}: {figura.__class__.__name__}")
        print(f"{figura}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        if isinstance(figura, Coloreado):
            print(f"Cómo colorear: {figura.comoColorear()}")

if __name__ == "__main__":
    main()
