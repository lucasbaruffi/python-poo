# Melhoria da classe criada anteriormente

# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto
    """
    def __init__(self, nome = "", idade = 0): # Método Construtor
        # Em vez de atribuir cada atributo, define direto no instanciamento
        # Atributos de Instância
        self.nome = nome
        self.idade = idade

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    # Isso retorna a mensagem quando pedir um print de um
    # objeto desta classe. Em vez de retornar a posição 
    # na memória (que é o padrão), vai retornar a frase.
    def __str__(self): # DUNDER Method
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."


# Declaração de Objetos
g1 = Gafanhoto("Maria", 17)
g1.aniversario()

print(g1)

# Mostra a documentação
print(g1.__doc__)

# Mostra os dados em forma de dicionário
# Isso serve para ver o estado atual do objeto
print(g1.__dict__) # {'nome': 'Maria', 'idade': 18}
print(g1.__getstate__()) # {'nome': 'Maria', 'idade': 18}

# Mostra a classe do atributo
print(g1.__class__) # <class '__main__.Gafanhoto'>