import math

class Algebravectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Algebravectorial(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, scalar):

        return Algebravectorial(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def Longitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normal(self):
        norm = self.Longitud()
        return Algebravectorial(self.x / norm, self.y / norm, self.z / norm)

    def productoescalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def productovectorial(self, other):
        return Algebravectorial(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
a = Algebravectorial(0, 5, 0)
b = Algebravectorial(4, 3, 0)
c = a + b
print(f"Suma: {c}")  
d = a * 2
print(f"Multiplicación por escalar: {d}")  

print(f"Longitud de a: {a.Longitud()}")  

e = a.normal()
print(f"Normal de a: {e}")  

productoescalarab = a.productoescalar(b)
print(f"Producto escalar a · b: {productoescalarab}") 

f = a.productovectorial(b)
print(f"Producto vectorial a × b: {f}")  
