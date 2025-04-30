from abc import ABC, abstractmethod

class Boleto(ABC):
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0

    def __str__(self):
        return f"Numero: {self.numero}, Precio: {self.precio}"

class Platea(Boleto):
    def __init__(self, numero, diasdeanticipacion):
        super().__init__(numero)
        if diasdeanticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0


class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0


class Galeria(Boleto):
    def __init__(self, numero, diasdeanticipacion):
        super().__init__(numero)
        if diasdeanticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0

def main():
    while True:
        print("Teatro Municipal")
        print("1. Boleto Palco")
        print("2. Boleto Platea") 
        print("3. Boleto Galeria")
        print("4. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            numero = int(input("Ingrese un numero de boleto: "))
            boleto = Palco(numero)
            print(boleto)
            
        elif opcion == "2":
            numero = int(input("Ingrese un numero de boleto: "))
            dias = int(input("Ingrese el numero de dias de anticipacion: "))
            boleto = Platea(numero, dias)
            print(boleto)
            
        elif opcion == "3":
            numero = int(input("Ingrese un numero de boleto: "))
            dias = int(input("Ingrese el numero de dias de anticipacion: "))
            boleto = Galeria(numero, dias)
            print(boleto)
            
        elif opcion == "4":
            print("Saliendo")
            break
        
        else:
            print("Ingrese una opcion valida :3 ")
            
if __name__ == "__main__":
    main()
