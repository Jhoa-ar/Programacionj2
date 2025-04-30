from Boleto import Boleto

class Palco(Boleto):
        def __init__(self, numero):
            super().__init__(numero)
            self.precio = 100.0
            