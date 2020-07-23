"""
Associação: uma classe se relaciona com outra,
 mas nenhuma classe depende da outra;
  podem 'viver' individualmente
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Ebert')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

# As 3 são independentes:
print(escritor.nome)
print(caneta.marca)
maquina.escrever()

# Fazendo associação:
escritor.ferramenta = maquina
escritor.ferramenta.escrever()