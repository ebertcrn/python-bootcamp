class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def muda_valor_lado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retorna_valor_lado(self):
        return self.tamanho_lado

    def calcula_area(self):
        return self.tamanho_lado ** 2

# teste da classe

q1 = Quadrado(40)
print(q1.retorna_valor_lado())
print(q1.calcula_area())
q1.muda_valor_lado(30)
print(q1.retorna_valor_lado())