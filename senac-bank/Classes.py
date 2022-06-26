
class Historico:
    def __init__(self, valorsaque, valordeposito):
        self.valorsaque  = valorsaque
        self.valordeposito = valordeposito

class Conta:
    def __init__(self, Cliente, numero, agencia, saldo, limite):
        print("Criando Conta")
        self.titular = Cliente
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo 
        self.limite = limite

    def sacar(self, valor):
        if valor <=0:
            print(f"Você não pode sacar {valor} R$, digite um valor positivo")
            exit()
        elif self.saldo >= valor :
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def depositar(self, valor):
        if valor >0 :
            self.saldo += valor
        else:
             print(f"Você não pode depositar {valor} R$, digite um valor positivo")

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        print("Criando Cliente")
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf; 



