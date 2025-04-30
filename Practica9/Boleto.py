from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0
        
    def __str__(self):
        return f"Numero: {self.numero}, Precio: {self.precio}" 