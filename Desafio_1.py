# Sistema bancário - Depósito, Saque, Extrato

#***************************DEPÓSITO***************************************************
#  Deve ser possível depositar valores positivos para a minha conta bancária. Para a V1 trabalhar apenas com 1 usuário (não sendo necessário identificar a conta)
# Todos os depósitos devem ser armazenados numa variável e exibido na operação de extrato
# FUNÇAO DEPÓSITO (POSITIONAL ONLY)

#***************************SAQUE******************************************************
#LIMITE DE SAQUE = 3
#VALOR LIMITE POR SAQUE = 500
#CASO NÃO TENHA SALDO SUFICIENTE O SISTEMA DEVERÁ INFORMAR (NÃO SERÁ POSSÍVEL SACAR O DINHEIRO POR FALTA DE SALDO)
#TODOS OS SAQUES DEVEM SER ARMAZENADOS E EXIBIDO NO EXTRATO
#FUNÇÃO SAQUE (KEYWORD ONLY)


#***************************EXTRATO******************************************************

#DEVE LISTAR OS DEPÓSITOS E OS SAQUES REALIZADOS NA CONTA. NO FIM DA LISTAGEM DEVE SER EXIBIDO O SALDO ATUAL DA CONTA 
#NO FIM DA LISTAGEM DEVE-SE EXIBIR O SALDO ATUAL DA CONTA
# FORMATO R$ xxx.xx
# FUNÇÃO EXTRATO (POSITIONAL ONLY E KEYWORD ONLY)

#***************************CADASTRO DE CLIENTES************************************************

# FUNÇAO CRIAR USUÁRIO: NOME; DATA DE NASCIMENTO, CPF, ENDEREÇO(LOGRADOURO, N, BAIRRO, CIDADE/SIGLA ESTADO)
# UM USUÁRIO POR CPF

#***************************** CRIAR CONTA****************************************************
# AGENCIA, NUMERO DE CONTA, USUÁRIO
# O NÚMERO DA CONTA INICIA EM 1.
# O NÚMERO DA AGENCIA É FIXO 0001
# UM USUÁRIO PODE TER MAIS DE 1 CONTA, MAS UMA CONTA PERTENCE A SOMENTE UM USUÁRIO

import textwrap

def menu():

    menu = """\n
    ________________ Menu _________________

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso!===")
            
    else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@@")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
     excedeu_saldo = valor > saldo
     excedeu_limite = valor > limite
     excedeu_saques = numero_saques >= limite_saques

     if excedeu_saldo:
          print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    
     elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")

     elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    
     elif valor>0:
         
         saldo -= valor
         extrato += f"Saque:\t\tR$ {valor:.2f}\n"
         numero_saque += 1

         print("\n=== Saque realizado com sucesso! ===")
     else:
        print("\n@@@ Operação falhou! Ovalor informado é inválido. @@@")
    
     return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
    print("\n======================= EXTRATO ==========================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("============================================================")

def criar_usuario(usuarios):

    cpf = input("informe o CPF (Somente numeros): ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input ("Informe o endereço (logradouro, n - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("=== Usuário criado com sucesso! ====")
     
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta}["usuario"]["nome"]
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
    



def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 1000
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
   

    while True:

        opcao = menu()

        if opcao =="d":
            valor = float(input("informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

            
        elif opcao == "s":
            valor = float(input("informe o valor do saque: "))


            saldo, extrato = sacar (

                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,

            )

        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
       
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")



main()