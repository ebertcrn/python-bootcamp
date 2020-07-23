from random import randint

class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método de instância => Precisa receber o parâmetro self (self se refere à própria instância)
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Não é referente à instância em si, mas sim é referente à classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # como se fosse uma função normal, fora da classe!
    @staticmethod # não precisa nem da instância, nem da classe!
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Ebert', 27)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

# utiliza a classe ou uma instância para usar o staticmethod
print(Pessoa.gera_id()) # pode gerar id pela classe
print(p1.gera_id()) # pode gerar id pela instancia