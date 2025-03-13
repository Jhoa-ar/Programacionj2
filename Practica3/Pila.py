class Pila:
    def __init__(self, n):
        self.top = 0
        self.n = n
        self.arreglo = [0] * (n + 1)

    def push(self, e):
        if self.top == self.n:
            print("Pila llena")
        else:
            self.top += 1
            self.arreglo[self.top] = e

    def pop(self):
        if self.top == 0:
            print("Pila vacia")
            return 0
        else:
            dato = self.arreglo[self.top]
            self.top -= 1
            return dato

    def peek(self):
        if self.top == 0:
            print("Pila vacia")
            return None
        return self.arreglo[self.top]

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top == self.n