from Palco import Palco
from Platea import Platea
from Galeria import Galeria

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