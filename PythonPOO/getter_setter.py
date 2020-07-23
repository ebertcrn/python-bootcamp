class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title() # letra inicial maiuscula

    # Getter: obtem um valor
    @property
    def preco(self):
        return self._preco

    # Setter: configura um valor
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): # checando se valor é uma instancia de string
            valor = float(valor.replace('R$','')) # substitui R$ por nada
            # ideal seria usar regex ao inves de replace()
        self._preco = valor



p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15') # float era esperado para desconto, por isso foi necessario adicionar o setter e o getter
p2.desconto(10)
print(p2.nome, p2.preco)