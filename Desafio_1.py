# Sistema bancário - Depósito, Saque, Extrato

#***************************DEPÓSITO***************************************************
#  Deve ser possível depositar valores positivos para a minha conta bancária. Para a V1 trabalhar apenas com 1 usuário (não sendo necessário identificar a conta)
# Todos os depósitos devem ser armazenados numa variável e exibido na operação de extrato

#***************************SAQUE******************************************************
#LIMITE DE SAQUE = 3
#VALOR LIMITE POR SAQUE = 500
#CASO NÃO TENHA SALDO SUFICIENTE O SISTEMA DEVERÁ INFORMAR (NÃO SERÁ POSSÍVEL SACAR O DINHEIRO POR FALTA DE SALDO)
#TODOS OS SAQUES DEVEM SER ARMAZENADOS E EXIBIDO NO EXTRATO


#***************************EXTRATO******************************************************

#DEVE LISTAR OS DEPÓSITOS E OS SAQUES REALIZADOS NA CONTA. NO FIM DA LISTAGEM DEVE SER EXIBIDO O SALDO ATUAL DA CONTA 
#NO FIM DA LISTAGEM DEVE-SE EXIBIR O SALDO ATUAL DA CONTA
# FORMATO R$ xxx.xx

menu = ''' 

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=>
'''

saldo = 1000
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao =="d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "s":
         valor = float(input("informe o valor do saque: "))

         excedeu_saldo = valor > saldo

         excedeu_limite = valor > limite

         excedeu_saque = numero_saque >= LIMITE_SAQUE

         if excedeu_saldo:
             print("Operação falhou! Você não tem saldo suficiente.")

         elif excedeu_limite:
             print("Operacção falhou! O valor do saque excede o limite")
         
         elif excedeu_saque:
             print("Operacção falhou! Número máximo de saque excedido")

         elif valor>0:
             saldo -= valor
             extrato += f"Saque: R$ {valor:.2f}\n"
             numero_saque += 1

         else:
             print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n======================= EXTRATO ==========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")