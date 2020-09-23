class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento


class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20


class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30


p1 = Programador("João", 20, 1000)
print(p1.nome)
print(p1.salario)
p1.aumenta_salario()
print(p1.salario)

a1 = Analista("Gisele", 18, 1500)
print(a1.nome)
print(a1.salario)
a1.aumenta_salario()
print(a1.salario)
