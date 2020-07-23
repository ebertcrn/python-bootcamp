"""
Agregação: uma classe depende da outra para funcionar corretamente,
embora ambas existam individualmente.
Ex:
Carro e Pneu: ambos existem individualmente, mas o carro só funcionará
corretamente se tiver pneus.
"""

from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 5000)
p3 = Produto('Caneca', 15)

# adicionar os produtos no carrinho de compras
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

# listar produtos no carrinho
carrinho.lista_produtos()

# valor total
print(carrinho.soma_total())