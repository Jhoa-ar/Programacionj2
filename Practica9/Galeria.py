from Boleto import Boleto

class Galeria(Boleto):
    def __init__(self, numero, diasdeanticipacion):
        super().__init__(numero)
        
        if diasdeanticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0