import math

def getDiscriminante(a,b,c):
    return b**2 - 4*a*c 

def getRaiz1(a, b, Discriminante):
    return -b - math.sqrt(Discriminante)/2*a

def getRaiz2(a, b, Discriminante):
    return -b + math.sqrt(Discriminante)/2*a     

def Resolver(a, b, c):
    discriminante = getDiscriminante(a, b, c)
    if discriminante > 0:
        raiz1 = getRaiz1(a, b, discriminante)
        raiz2 = getRaiz2(a, b, discriminante)
        print (f"La ecuacion tiene dos raices: {raiz1}, {raiz2}")
    elif discriminante == 0:
        raiz1 = -b / (2*a)
        print (f"La ecuacion tiene solo una raiz: raiz1 = {raiz1}")
    else:
        print ("La ecuacion no tiene raıces reales")

a = float(input("ingrese a: "))
b = float(input("ingrese b: "))
c = float(input("ingrese c: "))

Resolver(a, b, c)
        