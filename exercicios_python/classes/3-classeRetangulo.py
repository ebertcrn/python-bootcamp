class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def muda_valor_lados(self, nova_base, nova_altura):
        self.base = nova_base
        self.altura = nova_altura

    def retorna_valor_lados(self):
        return self.base, self.altura

    def calcula_area(self):
        return self.base * self.altura

    def calcula_perimetro(self):
        return (2 * self.base) + (2 * self.altura)

# teste da classe
ret = Retangulo(10, 20)
print(ret.retorna_valor_lados())
print(ret.calcula_area())
print(ret.calcula_perimetro())
print(ret.muda_valor_lados(30, 40))
print(ret.retorna_valor_lados())

# programa
base = float(input('Entre com um valor para a base (em metros): '))
altura = float(input('Entre com um valor para a altura (em metros): '))

local_cliente = Retangulo(base, altura)
print(f'A área do local é de {local_cliente.calcula_area()} metros quadrados.')
print(f'O perímetro do local é de {local_cliente.calcula_perimetro()} metros.')
