"""
Composição é a relação mais forte entre classes

- Uma classe pertence a outra

- Uma classe vai ser 'dona' de objetos de outra classe.
Isto é, se a classe principal for apagada,
todos os objetos que a classe principal utilizou
vão ser apagados com ela.
"""

from classes import Cliente

cliente1 = Cliente('Ebert', 27)
cliente1.insere_endereco('Florianopolis', 'SC')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3

print('################################################')