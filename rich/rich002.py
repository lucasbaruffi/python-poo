from rich import print
from rich.panel import Panel

caixa = Panel(
    "Esse é um painel de exemplo", 
    title="Mensagem", 
    style="red",
    width=50, 
) 


print(caixa)
