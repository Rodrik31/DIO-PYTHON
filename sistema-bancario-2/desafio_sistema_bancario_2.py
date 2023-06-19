import os
def limpar():
    os.system('cls') or None
limpar()

def menu():    
    print("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar usuário
    [q] Sair
    => """)
    opcao = input()
    return opcao

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    if valor > 500:
        print(f"Saque recusado.\nLimite de saque: R$ {limite:.2f}")
    elif valor <= 0:
        print("Erro, digite um valor positivo.")
    elif valor > saldo:
        print("Erro, o valor do saque é maior que saldo existente.")
    elif numero_saque == limite_saque:
        print("O valor não pode ser sacado.\nLimite diário de saques atingindo.")
    else:
        saldo -= valor
        numero_saque +=1
        extrato += f"Saque: R$ {valor:.2f}\n"
        limpar()
        print("Saque realizado com sucesso.")

    return saldo, extrato, numero_saque

def deposito(saldo, valor, extrato, /):
    if valor <= 0:
        print("Erro, digite um valor positivo.")
    else:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n" 
        limpar()
        print("Deposito realizado com sucesso.")         

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    limpar()
    if extrato:
        print(extrato + f"\nSaldo: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.") 
    return extrato

def cadastrar_usuario(CPF):
    return usuarios

def criar_conta_corrente(usuario):
    return contas_correntes

def main():    
    saldo = 0
    valor = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()

        if opcao == "d":
            limpar()
            valor = float(input("Digite o valor para depositar: "))
            saldo, extrato = deposito(saldo, valor, extrato)            
        elif opcao == "s":
            limpar()
            valor = float(input("Digite um valor para sacar:" ))
            saldo, extrato, numero_saques = saque(
                                                    saldo=saldo, 
                                                    valor=valor, 
                                                    extrato=extrato, 
                                                    limite=limite, 
                                                    numero_saque=numero_saques, 
                                                    limite_saque=LIMITE_SAQUES
                                                )            
        elif opcao == "e":
            extrato = exibir_extrato(saldo, extrato=extrato)
        elif opcao == "c":
            usuario = input()
            usuarios = cadastrar_usuario(usuario)     
        elif opcao == "q":
            input("Obrigado por utilizar nossos sistemas.")
            limpar()        
            break
        else:
            limpar()
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()