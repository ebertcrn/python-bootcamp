"""
Associacao: um objeto usa outro objeto
Agregacao: um objeto tem outro objeto
Composicao: um objeto é dono de outro objeto
Heranca: um objeto é outro objeto

"""

from classes import *

p1 = Pessoa('João', 19)
p1.falar()
# p1.estudar() = ERRO
# p1.falar.comprar() = ERRO

c1 = Cliente('Ebert', 27)
c1.falar()
c1.comprar()
# c1.estudar() = ERRO

a1 = Aluno('Rose', 60)
a1.falar()
a1.estudar()
# a1.comprar = ERRO