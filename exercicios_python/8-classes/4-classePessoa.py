class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhece(self):
        while self.idade < 21:
            self.altura += 0.5
            self.idade += 1

    def engorda(self, adiciona_peso):
        self.peso += adiciona_peso
        return self.peso

    def emagrece(self, diminui_peso):
        if diminui_peso > self.peso:
            print('Não pode emagrecer mais do que vc pesa.')
            self.peso = 0
        else:
            self.peso -= diminui_peso
        return self.peso

    def cresce(self, crescimento):
        return self.altura + crescimento

# teste da classe
p1 = Pessoa('João', 22, 80, 187)
p1.envelhece()
print(p1.engorda(10))
print(p1.emagrece(10))
print(p1.cresce(10))