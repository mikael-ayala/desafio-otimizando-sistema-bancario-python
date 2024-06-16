def menu():
    return '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar usuário
    [l] Listar usuários
    [cc] Criar conta
    [lc] Listar contas
    [q] Sair

    => '''

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito | R$ {valor:.2f}\n'
        print(f'Deposito de R$ {valor:.2f} foi efetuado com sucesso, saldo total de R$ {saldo:.2f}.')
    else:
        print('Depósito negado! O valor depositado precisa ser maior do que zero.')

    return saldo, extrato

def sacar(*, valor, saldo, extrato, numero_saques, limite_saques):
    if valor > 0 and valor <= saldo and numero_saques < limite_saques:
        saldo -= valor
        extrato += f'Saque    | R$ {valor:.2f}\n'
        numero_saques += 1
        print(f'Saque de R$ {valor:.2f} foi efetuado com sucesso, saldo total de R$ {saldo:.2f}.')
    elif numero_saques >= limite_saques:
        print('Saque negado! Limite de saques diários excedido.')
    elif valor > saldo:
        print('Saque negado! Valor de saque excede o valor de saldo disponível.')
    else:
        print('Saque negado! Valor de saque deve ser um número positivo.')

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print('====== Extrato =======')
    print(extrato)
    print(f'Saldo    | R$ {saldo:.2f}')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF (somente números): ')
    usuario_existe = filtrar_usuario(cpf, usuarios)

    if usuario_existe:
        print('\n Erro! CPF já cadastrado.')
        return

    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    endereco = input('Digite seu endereço(logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(f'\nParabéns {nome}, você foi cadastrado com sucesso!')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario_existe = filtrar_usuario(cpf, usuarios)

    if not usuario_existe:
        print('\n Erro! CPF não encontrado.')
        return
    
    usuario = [usuario for usuario in usuarios if usuario['cpf'] == cpf]

    return {'Agência': agencia, 'C/C': numero_conta, 'Nome Titular': usuario[0]['nome'], 'CPF Titular': usuario[0]['cpf']}

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    numero_conta = 1

    while True:

        opcao = input(menu())

        if opcao == 'd':
            valor = float(input('Digite o valor que deseja depositar: '))
            saldo, extrato = depositar(valor, saldo, extrato)

        elif opcao == 's':
            valor = float(input('Digite o valor que deseja sacar: '))
            saldo, extrato, numero_saques = sacar(valor=valor, saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)
            
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'c':
            criar_usuario(usuarios)

        elif opcao == 'l':
            print(usuarios)

        elif opcao == 'cc':
            nova_conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if nova_conta:
                contas.append(nova_conta)
                numero_conta += 1
                print('Conta criada com sucesso!')

        elif opcao == 'lc':
            print(contas)

        elif opcao == 'q':
            break
        
        else:
            print('Operação inválida, por favor selecione novamente a operação desejada.')

main()