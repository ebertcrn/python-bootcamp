class Pessoa:
    ano_atual = 2020 # atributo de classe

    def __init__(self, nome, idade): # atributos relacionados à instancia
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self): # atributos relacionados à instancia
        print(self.ano_atual - self.idade)

    # criar a pessoa baseado no ano de nascimento, e não na idade
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): # cls é o self (pode ser qlqr nome)
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade) # retorna a propria classe

# Método de Instância vs Método de Classe
# Pensar: esse método que está sendo criado é relacionado à classe em geral, ou à instância (específico de cada objeto)?


p1 = Pessoa('Ebert',27)
print(Pessoa.ano_atual)

# para chamar o metodo get_ano_nascimento, é preciso passar uma instancia:
p2 = Pessoa('Luiz', 63)
p2.get_ano_nascimento()

print(p1.idade) # 27
p1.get_ano_nascimento() # 1993

p3 = Pessoa.por_ano_nascimento('Ebert', 1993)
print(p3) # <__main__.Pessoa object at 0x7fba6010e160>
print(p3.nome, p3.idade) # Ebert 27
p3.get_ano_nascimento() # 1993