"""
Encapsulamento: proteger sua aplicação!

metodos e atributos public, protected e private
1) public: metodos e atributos que podem ser acessados dentro e fora da classe
2) protected: atributos que podem ser acessados apenas dentro da classe ou das filhas dessa classe
3) private: atributo ou método só está disponível dentro da classe

No Python, foram criadas algumas convenções:
1) _ : PRIVATE/PROTECTED (public com _ no nome) -> recomenda-se que vc não acesse esse atributo!
2) __ : PRIVADO (_NOMECLASSE__noteatributo) -> recomenda-se FORTEMENTE que vc não acesse esse atributo!
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {} # deveria ser um atributo privado ou protected

    @property
    def dados(self): # 'dados' passa a ser uma propriedade da classe
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Ebert')
bd.inserir_cliente(2, 'Rose')

bd.__dados = 'Outra coisa'

print(bd.__dados) # Outra coisa
print(bd._BaseDeDados__dados) # {'clientes': {1: 'Ebert', 2: 'Rose'}}

bd2 = BaseDeDados()
bd2.inserir_cliente(1, 'Maria')
bd2.inserir_cliente(2, 'João')
print('bd2:')
bd2.lista_clientes()

# agora podemos acessar a propriedade 'dados' através do seguinte comando:
print(bd2.dados)
