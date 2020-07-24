class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)

# teste da classe

b1 = Bola('Azul', 30, 'Couro')
b1.mostraCor()

b1.trocaCor('Vermelho')
b1.mostraCor()