# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # O self é para indicar quem chamou
        # Atributos de Instância
        self.nome = ""
        self.idade = 0
        self.peso = 0.0

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto, tem {self.peso:.2f}kg e tem {self.idade} anos de idade."

    def comer(self):
        self.peso += 3

    def jejuar(self):
        self.peso -= 2


# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.peso = 60
g1.aniversario()
print(g1.mensagem())
g1.comer()
print(g1.mensagem())
g1.comer()
print(g1.mensagem())
g1.jejuar()
print(g1.mensagem())


g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
print(g2.mensagem())