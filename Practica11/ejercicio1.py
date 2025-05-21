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
        
       
# main
a1 = Artista("Jhoana Calderon", "13788898", 25)
a2 = Artista("Nayeli Cuenca", "14578965", 12)

anuncio1 = Anuncio(45245, 1250)


pintura = Pintura("Gabriel Garcia Marquez", "Lienzo", a1, a2, "drama", anuncio1)


pinturaSin = Pintura("Jhoana Nicol Calderon", "Pinturas oleo", a1, a2, "tristeza")

pintura.mostrar()
pinturaSin.mostrar()

artistas = [
    pintura.artista1,
    pintura.artista2,
    pinturaSin.artista1,
    pinturaSin.artista2
]


artista_experto = artistas[0]


for artista in artistas[1:]:
    if artista.añosExperiencia > artista_experto.añosExperiencia:
        artista_experto = artista

print("Artista con más años de experiencia:")
artista_experto.mostrar()

nuevo_anuncio = Anuncio(99999, 850)  
pinturaSin.anuncio = nuevo_anuncio

totalventa = 0

for pinturaactual in [pintura, pinturaSin]:
    if pinturaactual.anuncio:
        totalventa += pinturaactual.anuncio.precio


print(f"\nMonto total de venta de ambas pinturas: {totalventa}")