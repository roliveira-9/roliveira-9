import textwrap

def menu():
    menu = '''\nDigite o número correspondente a operação que deseja realizar: \n 
    ==================== MENU ====================
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tAbrir Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair
    '''
    return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===\n')
        print(f'\nSaldo Atual:\t\tR$ {saldo:.2f}')
    else:
        print('\n=== Operação falhou! O valor informado é inválido. ===\n')

    return saldo,extrato


def sacar(*, saldo, valor,extrato,limite,num_saques,limite_saques):
    if valor > saldo:
        print('\n=== Operação falhou! Você não tem saldo sufuciente. ===\n') 
        print(f'\nSaldo Atual:\t\tR$ {saldo:.2f}')
    elif valor > limite:
        print('\n=== Operação falhou! O valor informado excede o limite. ===\n') 
    elif num_saques >= limite_saques:
        print('\n=== Operação falhou! Número máximo de saques excedido. ===\n')
    elif valor > 0:
        saldo -= valor
        extrato = f'Saque:\t\tR$ {valor:.2f}\n'
        num_saques += 1
        print('\n=== Saque realizado com sucesso! ===\n')
        print(f'\nSaldo Atual:\t\tR$ {saldo:.2f}')
    else:
        print('\n=== Operação falhou! O valor informado é inválido. ===\n')
    
    return saldo,extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=========================================')


def cadastrar_usuario(usuarios):
    cpf = input('\nInforme o CPF (somente números): ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('\n=== Já existe usuário com este CPf! ===')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço completo (logradouro - número -bairro - ciddade/uf): ')

    usuarios.append({'nome': nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereco})

    print('\n=== Usuário cadastrado com sucesso! ===\n')

def filtrar_usuarios(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuarios(cpf,usuarios)

    if usuario:
        print('\n=== Conta criada com sucesso! ===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('\n=== Usuário não encontrado, fluxo de criação encerrado! ===')


def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C\C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0365'


    saldo = 1000
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor do deposito: '))

            saldo, extrato = depositar( saldo,valor,extrato)

        elif opcao == '2':
            valor = float(input(" Informe o valor de saque: "))

            saque,extrato = sacar(
                saldo= saldo,
                valor= valor,
                extrato=extrato,
                limite= limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao =='3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '6':
            cadastrar_usuario(usuarios)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta,usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '5':
            listar_contas(contas)
        
        elif opcao == '0':
            break

        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')


main()