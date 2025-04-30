from Boleto import Boleto

class Platea(Boleto):
    def __init__(self, numero, diasdeanticipacion):
        super().__init__(numero)
        if diasdeanticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0
            
            