class Artista:
    def __init__(self, nombre , ci , añosExperiencia):
        self.nombre = nombre
        self.ci = ci 
        self.añosExperiencia = añosExperiencia
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}, CI: {self.ci}, Años de Experiencia: {self.añosExperiencia}")
    
class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        
    def mostrar(self):
        print(f"Anuncio: {self.numero}, Precio: {self.precio}")
        
class Obra:
    def __init__(self, titulo, material, artista1: Artista, artista2: Artista, anuncio: Anuncio = None):
        self.titulo = titulo
        self.material = material
        self.artista1 = artista1
        self.artista2 = artista2
        self.anuncio = anuncio
        
    def mostrar(self):
        print(f"Obra: {self.titulo}")
        print(f"Material: {self.material}")
        print("Artistas:")
        self.artista1.mostrar()
        self.artista2.mostrar()
        if self.anuncio:
            self.anuncio.mostrar()
        else:
            print("Sin anuncio")
        
class Pintura(Obra):
    def __init__(self, titulo, material, artista1, artista2, genero, anuncio=None):
        super().__init__(titulo, material, artista1, artista2, anuncio)
        self.genero = genero
        
    def mostrar(self):
        super().mostrar()
        print(f"Género: {self.genero}") 
        

a1 = Artista("Jhoana Calderon", "13788898", 25)
a2 = Artista("Nayeli Cuenca", "14578965", 12)

anuncio1 = Anuncio(45245, 1250)
anuncio2 = Anuncio(99999, 850)

pintura1 = Pintura("Gabriel Garcia Marquez", "Lienzo", a1, a2, "drama", anuncio1)
pintura2 = Pintura("Jhoana Nicol Calderon", "Pintura oleo", a1, a2, "tristeza", anuncio2)

pintura1.mostrar()
print()
pintura2.mostrar()

artistas = [
    pintura1.artista1,
    pintura1.artista2,
    pintura2.artista1,
    pintura2.artista2
]

suma_experiencia = 0
cantidad_artistas = len(artistas)

for i in range(cantidad_artistas):
    suma_experiencia += artistas[i].añosExperiencia

promedio_experiencia = suma_experiencia / cantidad_artistas

print(f"\nPromedio de años de experiencia de los artistas: {promedio_experiencia:.2f}")

nombre_artista_a_incrementar = "Jhoana Calderon"
incremento_precio = 200

for pintura in [pintura1, pintura2]:
    if pintura.artista1.nombre == nombre_artista_a_incrementar or pintura.artista2.nombre == nombre_artista_a_incrementar:
        if pintura.anuncio:  
            pintura.anuncio.precio += incremento_precio
            print(f"\nSe incrementó el precio del anuncio de la pintura '{pintura.titulo}' en {incremento_precio}")
            pintura.anuncio.mostrar()
        else:
            print(f"\nLa pintura '{pintura.titulo}' no tiene anuncio para incrementar el precio.")

print("\nPrecios finales de las pinturas:")
for pintura in [pintura1, pintura2]:
    if pintura.anuncio:
        print(f"Pintura: {pintura.titulo}, Precio: {pintura.anuncio.precio}")
    else:
        print(f"Pintura: {pintura.titulo}, Sin anuncio")
