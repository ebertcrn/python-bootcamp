class Tamagotchi:
    humor = None

    def __init__(self, nome=None, fome=False, saude=True, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def altera_nome(self, novo_nome):
        self.nome = novo_nome
        print(self.nome)

    def verifica_fome(self):
        if not self.fome:
            print('Tamagotchi está alimentado.')
        else:
            print('Tamagotchi está com fome.')
            self.fome = True
            print('Tamagotch foi alimentado.')

    def verifica_saude(self):
        if not self.saude:
            print('Tamagotchi não está saudável.')
        else:
            print('Tamagotchi está saudável.')

    def verifica_idade(self):
        print(self.idade)

    def verifica_humor(self):
        if not self.fome and not self.saude:
            humor = False
            print('Tamagotchi está mal humorado.')
        else:
            print('Tamagotchi está bem humorado.')

# teste da classe
tama1 = Tamagotchi()
tama1.altera_nome('João')
tama1.verifica_fome()
tama1.verifica_saude()
tama1.verifica_idade()
tama1.verifica_humor()