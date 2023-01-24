import os
def limpar():
    os.system('cls') or None

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        limpar()
        print('deposito realizado')

    elif opcao == "s":
        limpar()
        print('saque realizado')



    elif opcao == "e":
        limpar()
        print('extrato realizado')


    
    elif opcao == "q":
        limpar()
        break

    else:
        limpar()
        print("Operação inválida, por favor selecione novamente a operação desejada.")