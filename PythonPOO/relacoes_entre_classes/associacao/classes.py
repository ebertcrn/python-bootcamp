class Escritor:
    def __init__(self, nome):
        self.__nome = nome # construtor já está fazendo o papel de setter
        self.__ferramenta = None

    # getter
    @property
    def nome(self):
        return self.__nome

    @property # getter
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter # setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca # setter

    # getter
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')