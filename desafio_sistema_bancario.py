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
        deposito = float(input("Digite o valor para depositar: "))
        if deposito <= 0:
            print("Erro, digite um valor positivo.")
        else:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
           

    elif opcao == "s":
        limpar()
        saque = float(input("Digite um valor para sacar:" ))
        if saque > 500:
            print(f"Saque recusado. Limite de saque: R$ {limite:.2f}")
        elif saque <= 0:
            print("Erro, digite um valor positivo.")
        elif saque > saldo:
            print("Erro, o valor do saque é maior que saldo existente.")
        elif numero_saques > 2:
            print("O valor não pode ser sacado.\nLimite diário de saques atingindo.")
        else:
            saldo -= saque
            numero_saques +=1
            extrato += f"Saque: R$ {saque:.2f}\n"



    elif opcao == "e":
        limpar()
        if extrato:
            print(extrato + f"\nSaldo: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações.")


    
    elif opcao == "q":
        limpar()
        break

    else:
        limpar()
        print("Operação inválida, por favor selecione novamente a operação desejada.")