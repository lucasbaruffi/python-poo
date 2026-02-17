from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome")
tabela.add_column("Preço")

tabela.add_row("Lápis", "1,50")
tabela.add_row("Caneta", "3,00")


print(tabela)