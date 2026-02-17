# Erros mais bonitos

from rich.traceback import install
install()

def divisao(x, y):
    return x / y

print(divisao(5, 0))