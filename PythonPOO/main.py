# do arquivo pessoa.py está importando a classe Pessoa
from pessoa import Pessoa

# Para criar um objeto a partir de uma classe, é preciso instanciar esse objeto!
p1 = Pessoa('Ebert',27)
p2 = Pessoa('João', 40)

# independencia entre os objetos da instancia
p1.falar('futebol')
p2.falar('basquete')

p1.parar_falar()
p2.comer('frango')

# Checando variável da classe (todos os objetos da classe terão acesso à essa variável)
print(p1.ano_atual)
print(p2.ano_atual)

# usando a classe em si (não estamos instanciando ela em lugar algo)
print(Pessoa.ano_atual)

nascimentoEbert = p1.get_ano_nascimento()
print(nascimentoEbert)