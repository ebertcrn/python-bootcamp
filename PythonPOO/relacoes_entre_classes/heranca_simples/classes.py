# Chamada de Super Classe / Mãe
class Pessoa:
    # O construtor da classe Pessoa será herdado tanto para a classe Cliente quanto para a classe Aluno
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    # falar() está na super classe, então pertence tanto a classe Cliente quanto a classe Aluno
    def falar(self):
        print(f'{self.nomeclasse} falando...')

"""
Chamadas de Sub Classes / Filhas: são classes mais especializadas; melhoram/especificam a super classe.

Ex: Cliente e Aluno são Pessoa, mas não necessariamente Pessoa é um Aluno.
"""

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')