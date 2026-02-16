class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}.")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque negado de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")

# Teste usando terminal para o git

c1 = ContaBancaria(112, "Gustavo", 3000)

# print(c1) # A conta 112 de Gustavo tem R$3,000.00
# print(c1.__doc__) # Cria uma conta bancária e permite fazer saques e depósitos.

# c1.depositar(500)
# c1.sacar(2000)
# print(c1) # A conta 112 de Gustavo tem R$1,500.00 de saldo

# c1.depositar(500)
# c1.sacar(2000000)
# print(c1) # 
# Conta 112 criada com sucesso. Saldo atual de R$3,000.00.
# Deposito de R$500.00 autorizado na conta 112
# Saque negado de R$2,000,000.00 na conta 112: SALDO INSUFICIENTE
# A conta 112 de Gustavo tem R$3,500.00 de saldo