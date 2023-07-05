# MENU DE OPÇÕES
menu = '''

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

'''

 # INFORMAÇÕES DA CONTA BANCÁRIA
saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:
    # FUNCIONALIDADES

    # Interação com o Cliente:
    opcao = input(f'\nInforme o número da operação que deseja realizar\n {menu}')

    # Operação de Depósito:
    if opcao == '1':
        valor = float(input('Informe o valor do depósito: R$ '))
        if valor >0:
            saldo += valor
            extrato += f'Depósito no valor de: R$ {valor:.2f}\n'
            print('\nDepósito realizado com sucesso!\n', 70 * '=' )
        else:
            print('Operação falhou! O valor informado é inválido.')


    # Operação de Saque:
    elif opcao == '2':
        valor = float(input('Informe o valor de saque: R$ '))
        
        # Verificar se o valor informado excede os limites da conta
        if valor > saldo:
            print('Operação falhou! Saldo insuficiente')
        elif valor > limite:
            print('Operação falhou! O valor de saque excede o limite')
        elif num_saques >= LIMITE_SAQUES:
            print('Operação falhou! Número máximo de saques excedido')

        # Saque
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de: {valor:.2f}\n' 
            print('\nSaque realizado com sucesso!\n')
            print(f'Saldo remanescente: R$ {saldo:.2f}\n', 70 * '=')  
            num_saques += 1
        else:
            print('Operação falhor! o valor informado é inválido')


    # Operação de Extrato:
    elif opcao == '3':
        print('\n==================== EXTRATO ====================')
        print('Não foram realizadas movimentações nesta conta.' if not extrato else extrato)
        print(f'\nSaldo atual: R$ {saldo:.2f}')
        print('=================================================')


    # Operação de Finalizar:
    elif opcao == '0':
        print('Operação Finalizada!','\nObrigado por utilizar nossos serviços.\n')
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')