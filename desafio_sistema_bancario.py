import os
def limpar():
    os.system('cls') or None
limpar()

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
        deposito = float(input("Digite o valor a ser depositado: "))
        if deposito <= 0:
            print("Erro, digite um valor positivo.")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
           

    elif opcao == "s":
        limpar()
        print('saque realizado')


    elif opcao == "e":
        limpar()
        extrato += f"\nSaldo: R$ {saldo:.2f}"
        print(extrato)


    
    elif opcao == "q":
        limpar()
        break

    else:
        limpar()
        print("Operação inválida, por favor selecione novamente a operação desejada.")