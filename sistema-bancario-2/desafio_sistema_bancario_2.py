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
    [cc] Criar Conta Corrente
    [lc] Listar contas
    [q] Sair""")
    opcao = input("\nEscolha uma operação: ")
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

def cadastrar_usuario(*, nome, usuarios, contas):
    limpar()
    CPF = input("Informe um CPF para cadastrar.\nNão use espaços, pontos ou traços.\nUse somente números.\n>>>")
    if CPF:
        resultado = filtrar_usuarios(CPF, usuarios)
        if not resultado:
            return
    else:
        return
    
    nome_completo = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço no seguinte modelo:\nlogradouro - nro - bairro - cidade/sigla do estado")
    novo_usuario = {
        "nome":nome,
        "nome_completo":nome_completo,
        "CPF":CPF,
        "data_nascimento":data_nascimento,
        "endereço":endereco
                    }
    usuarios.append(novo_usuario)
    criar_conta_corrente(novo_usuario, contas)
    limpar()
    return usuarios

def filtrar_usuarios(CPF, usuarios):
    if len(CPF) != 11:
        print("Digite um CPF válido.")
        return False
    else:
        for usuario in usuarios:
            if usuario["CPF"] == CPF:
                print("Usuário já cadastrado com o CPF fornecido.")
                return False
        return True


def criar_conta_corrente(usuario, contas):
    numero_conta = len(contas) + 1
    nova_conta = {
        "usuário":usuario["nome"],
        "nome":usuario["nome_completo"],
        "número_conta":numero_conta,
        "agência":"0001",}
    
    contas.append(nova_conta)          
    return contas

def listar_contas(contas):
    limpar()
    if not contas:
        print("Não existem contas cadastradas.")
        return        
    for conta in contas:  
        dados = f"""\n
        Agência:\t{conta["agência"]}
        C/C:\t\t{conta["número_conta"]}
        Títular:\t{conta["nome"]}            
        """        
        print(dados)
    input()
    limpar()
        

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
            nome = input("Informe o nome do usuário: ")
            usuarios = cadastrar_usuario(nome=nome, usuarios=usuarios, contas=contas)            
        elif opcao == "lc":
            listar_contas(contas)  
        elif opcao == "cc":
            limpar()
            CPF = input("Informe um CPF para verificação.\nNão use espaços, pontos ou traços.\nUse somente números.\n>>>")            
            cpf_existe = False
            for usuario in usuarios:
                if usuario["CPF"] == CPF:
                    cpf_existe = True
                    contas = criar_conta_corrente(usuario, contas)                    
                    break

            if not cpf_existe:
                print("CPF não encontrado nos usuários.\nCadastre um usuário primeiro, antes de criar uma conta.")            

        elif opcao == "q":
            input("Obrigado por utilizar nossos sistemas.")
            limpar()        
            break
        else:
            limpar()
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()