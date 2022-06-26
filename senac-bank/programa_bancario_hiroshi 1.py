
from Classes import Conta, Cliente, Historico
from datetime import datetime 

# Fazendo cadastro
resposta_usuario = int(input("Digite uma opção: "
            "\n\n 1 - Logar \n 2- Cadastrar\n"))

# printa o menu principal 
def menu_principal():

    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Encerrar Sessão")
    print("4 - Exibir Historico")
    print("5 - Exibir Extrato")


# faz o cadastro do cliente e da conta
if resposta_usuario == 2:
    
    print("Realizando cadastro:")
    print("------------------------------------------------------------------")
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    cpf = input("Digite seu CPF: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    print("------------------------------------------------------------------\n")

    new_cliente = Cliente(nome, sobrenome, cpf)
    new_conta = Conta(new_cliente, 123-4, 0000-1, saldo_inicial, 1000.00)

# Indica que a função esta em desenvolvimento
elif resposta_usuario == 1:
    print("A função ainda esta em fase de desenvolvimento")
    exit()

# Não deixa o usuario digitar qualquer numero
elif resposta_usuario != 1 or resposta_usuario != 2 :
    print("Resposta invalida, digite a opção 1 ou opção 2")
    exit()

# Imprime lista e pergunta qual ação deve 3
# ser realizada
menu_principal()
opcao_escolhida = int(input("\nQual ação você quer realizar? "))
valorsaque = []
valordeposito = []

while (opcao_escolhida != 3):
    # realiza o saque
    if opcao_escolhida == 1:
        print("\nVocê escolheu a opção de saque")
        print("------------------------------------------------------------------")
        valor = float(input("Quanto você deseja sacar? "))
        new_conta.sacar(valor)
        print("------------------------------------------------------------------\n")
    
        valorsaque.append(valor)
        menu_principal()

    # realiza o deposito
    if opcao_escolhida == 2:
        print("\nVocê escolheu a opção de deposito")
        print("------------------------------------------------------------------")
        valor = float(input("Quanto você deseja depositar? "))
        new_conta.depositar(valor)
        print("------------------------------------------------------------------\n")

        valordeposito.append(valor)
        menu_principal()

    # Emitir historico
    if opcao_escolhida == 4:
        print("\nEmitindo seu histórico")
        print("------------------------------------------------------------------")
        print("Transações ja realizadas:")
        new_historico = Historico(valorsaque, valordeposito)

        if len(valorsaque) == 0 and len(valordeposito) == 0:
            print("Você ainda não fez nenhum saque ou deposito")

        for valor in valorsaque:
            print((f"--> saque de {valor} R$"))

        for valor in valordeposito:
            print((f"--> deposito de {valor} R$"))

        print("------------------------------------------------------------------\n")

        menu_principal()

    # Exibir extrato
    if opcao_escolhida == 5:
        print("\nExibindo seu extrato:")
        print("------------------------------------------------------------------")
        print(f"Titular da conta: {new_conta.titular.nome} {new_conta.titular.sobrenome}")
        print(f"Saldo atual da conta: {new_conta.saldo}")
        print(f"Saldo atualizado em: {datetime.now()}")
        print("------------------------------------------------------------------\n")

        menu_principal()

    opcao_escolhida = int(input("\nQual ação você quer realizar? "))

# encerrando a sessão
if opcao_escolhida == 3:
    print("\nSessão encerrada.")
    exit()