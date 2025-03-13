import math
import matplotlib.pyplot as plt
import numpy as np

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = math.sqrt(self.x**2 + self.y**2)  
        self.theta = math.atan2(self.y, self.x)

    def coord_cartesianas(self):
        return (self.x, self.y)

    def coord_polares(self):
        return (self.r, self.theta)

    def __str__(self):
        return f"Punto Cartesianas: ({self.x:.2f}, {self.y:.2f}), Polares: ({self.r:.2f}, {self.theta:.2f})"

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea: {self.p1}, {self.p2}"

    def dibuja_linea(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def grafica_linea(self):
        plt.plot([self.p1.x, self.p2.x], [self.p1.y, self.p2.y], label='Línea', color='blue')

class Circulo:
    def __init__(self, c, r):
        self.centro = c
        self.radio = r

    def __str__(self):
        return f"Circulo: Centro={self.centro}, Radio={self.radio}"

    def grafica_circulo(self):
        theta = np.linspace(0, 2 * np.pi, 100)
        x = self.centro.x + self.radio * np.cos(theta)
        y = self.centro.y + self.radio * np.sin(theta)
        plt.plot(x, y, label='Círculo', color='red')


r1 = Punto(0, 5)
p1 = Punto(0, 0) 
p2 = Punto(5, 5)  

print("Coordenadas Cartesianas =", r1.coord_cartesianas())
print(f"Coordenadas Polares = ({r1.coord_polares()[0]:.2f}, {r1.coord_polares()[1]:.2f})")
print(r1)

linea = Linea(p1, p2) 
print(linea)
print(f"Dibuja linea: {linea.dibuja_linea():.2f}")


linea.grafica_linea()
circulo = Circulo(r1, 5) 
circulo.grafica_circulo()


plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Dibujo de Línea y Círculo')
plt.legend()
plt.grid()
plt.axhline(0, color='black',linewidth=0.5, ls='--')  
plt.axvline(0, color='black',linewidth=0.5, ls='--')  
plt.show()