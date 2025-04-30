import random
from cuadrado import Cuadrado
from circulo import Circulo
from colorear import Coloreado

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


