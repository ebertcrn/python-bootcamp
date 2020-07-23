class A:
    # variavel de classe
    varClasse = 123

    def __init__(self):
        # variavel de instancia
        self.varClasse = 321

a1 = A()
a2 = A()

print(a1.varClasse)
print(a2.varClasse)
print(A.varClasse)

# podemos alterar o valor de varClasse:
A.varClasse = 'Alterado'

print(a1.varClasse)
print(a2.varClasse)
print(A.varClasse)