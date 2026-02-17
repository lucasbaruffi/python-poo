from rich import print
from rich import inspect

class Funcionario:
    '''
    Cria um funcionário com Nome, Setor e Cargo de uma empresa fictícia.
    '''
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}."

f1 = Funcionario("Lucas", "TI", "Desenvolvedor RPA")
print(f1.apresentacao())
# print(f1.__dict__)
# inspect(f1, all=True)
# inspect(Funcionario) 

# Ao alterar o Atributo da Classe, todos os objetos recebem esse novo valor!
Funcionario.empresa = "Google"

print(f1.apresentacao())