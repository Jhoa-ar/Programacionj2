import random
class Juego:
    def __init__(self,numeroDeVidas, record):
        self.numeroDeVidas = numeroDeVidas
        self.record = record
    def reiniciaPartida(self):
        return None
    def actualizaRecord(self):
        return None
    def quitaVida(self):
        self.numeroDeVidas -= 1
        print(f"Te quedan {self.numeroDeVidas} vidas.")
        
        if self.numeroDeVidas > 0:
            return True
        else:
            return False
            
    
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas, record,):
        super().__init__(numeroDeVidas, record)
        self.numeroAAdivinar = random.randint(0, 10)
        
    def Juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        
        while True:
            print(f"Adivina el numero entre el 0 y el 10")
            jugar = int(input("Introduzca un numero: "))
            
            if not self.validaNumero(jugar):
                print("Introduce un número válido")
                continue

            if jugar == self.numeroAAdivinar:
                print(f"Acertaste!!")
                self.actualizaRecord()
                break  
            else:
                print(f"Fallaste :(")
                
                    
                if not self.quitaVida():
                    print(f"No tienes mas vidas")
                    break 
                    
                if jugar < self.numeroAAdivinar:
                    print("El número a adivinar es mayor.")
                else:
                    print("El número a adivinar es menor.")
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            return True
        else:
            return False
        
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas, record):
        super().__init__(numeroDeVidas, record)
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        else: 
            print(f"Introduzca un numero par")
            return False         
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def __init__(self, numeroDeVidas, record):
        super().__init__(numeroDeVidas, record)
        
    def validaNumero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        else: 
            print(f"Introduzca un Numero impar")
            return False  
        
class Aplicacion:
    def main(self):
        juego1 = JuegoAdivinaNumero(3, 0)
        juego2 = JuegoAdivinaPar(3,0)
        juego3 = JuegoAdivinaImpar(3,0)
        
        print(f"Comenzo el juego adivina numero: ")
        juego1.Juega()
        
        print(f"Adivina par: ")
        
        juego2.Juega()
        
        print(f"Adivina impar: ")
        
        juego3.Juega()
        
if __name__ == "__main__":
    app = Aplicacion()
    app.main()    