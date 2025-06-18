import textwrap

sistema_boas_vindas = """
=============================================
===== Seja bem-vindo ao banco Python 🐍 =====
=============================================
""".upper()

sistema_exit = """
==============================================
=== Obrigado por utilizar nossos serviços! ===
==============================================
""".upper()

def menu():
    menu_input = """\n
    ============== MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [1]\tCadastrar Usuário
    [2]\tCriar Conta
    [3]\tFiltrar Usuários
    [4]\tListar Contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_input))

def validador_input(valor, **kwargs):
    dados = [dado for dado in valor]

    for dado in dados:
        if dado in kwargs.values():
            return True

def depositar(saldo, valor, extrato, /,):
    if valor > 0:
        saldo += valor
        extrato += f">>> Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    print(f">>> Depósito realizado!\n\n>>> Saldo atual: R$ {saldo:.2f}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(f"Falha! Você não tem saldo suficiente para realizar essa operação.\n>>> Saldo atual: {saldo:.2f}")

    elif excedeu_limite:
        print(f"Falha! O valor do saque excede o limite permitido de R$ {limite:.2f}.\n>>> Saldo atual: {saldo:.2f}")

    elif excedeu_saques:
        print(f"Número de saques diários excedidos. Não é possível realizar mais saques.")

    elif valor > 0:
        saldo -= valor
        extrato += f">>> Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f">>> Saque realizado!\n\n>>> Saldo atual: R$ {saldo:.2f}")

    else:
        return print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def ver_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return saldo

def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    if cpf == "":
        print("CPF em branco! Por favor, tente novamente.")
        return
    
    cpf_invalido = validador_input(cpf, kwarg1=".", kwarg2="-", kwarg3="/")
    
    if cpf_invalido:
        print("CPF inválido! Por favor, tente novamente.")
        return
    
    existe_cpf = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    if existe_cpf:
        print("Ja existe um usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    
    if nome == "": 
        print("Nome em branco! Por favor, tente novamente.")
        return
    
    data_nascimento = input("informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("=" * 100)
    print(f"Usuário cadastrado com sucesso! Seja bem-vindo, {nome}!".upper())
    return usuarios

def criar_conta(usuarios, contas, /, *, numero_contas, numero_agencia):
    cpf_usuario_input = input("Informe o CPF do usuário (somente números): ")
    cpf_invalido = validador_input(cpf_usuario_input, kwarg1=".", kwarg2="-", kwarg3="/")
    
    if cpf_invalido:
        print("CPF inválido! Por favor, tente novamente.")
        return numero_contas, numero_agencia

    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf_usuario_input]
    
    if not usuario_encontrado:
        print("Falha ao criar conta! O usuário não existe.")
        return numero_contas, numero_agencia
    
    numero_contas += 1
    numero_agencia += 1
    agencia_formatado = f"{numero_agencia:04d}"
    contas.append({"agencia": numero_agencia, "numero_conta": agencia_formatado, "usuario": usuario_encontrado[0]})

    print(f">>> Conta cadastrada com sucesso!\n\n>>> Agência: {agencia_formatado} || Conta: {numero_contas} || Titular: {usuario_encontrado[0]['nome']}")
    return numero_contas, numero_agencia

def filtrar_usuario(usuarios, contas):
    todos_usuarios = [usuario for usuario in usuarios]
    todas_contas = [conta for conta in contas]
    
    if todos_usuarios == []:
        print("Nenhum usuário cadastrado.")
        return
    
    cpf_usuario_input = input("Informe o CPF do usuário (somente números): ")
    cpf_invalido = validador_input(cpf_usuario_input, kwarg1=".", kwarg2="-", kwarg3="/")
    
    if cpf_invalido:
        print("CPF inválido! Por favor, tente novamente.")
        return
    
    verificar_usuario = [usuario for usuario in todos_usuarios if usuario["cpf"] == cpf_usuario_input]
    
    if not verificar_usuario:
        print("Usuário não encontrado.")
        return
    
    qnt_contas_usuario = [conta for conta in todas_contas if conta["usuario"]["cpf"] == cpf_usuario_input]
    print(f"Nome: {verificar_usuario[0]['nome']} - CPF: {verificar_usuario[0]['cpf']} - Quantidade de contas: {len(qnt_contas_usuario)}\n")

def listar_contas(contas):
    if contas == []:
        print("Nenhuma conta criada.")
        return
    
    todas_contas = [conta for conta in contas]

    for conta in todas_contas:
        print(f"Agência: {conta['agencia']} || Conta: {conta['numero_conta']} || Titular: {conta['usuario']['nome']}")

def main():
    usuarios = []
    contas = []

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    numero_contas = 0
    numero_agencia = 0
    
    print(sistema_boas_vindas)

    while True:
        opcao = menu()
        
        if opcao == "d":
            deposito_input = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, deposito_input, extrato)

        elif opcao == "s":
            saque_input = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=saque_input,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            ver_extrato(saldo, extrato=extrato)
            
        elif opcao == "1":
            cadastrar_usuario(usuarios)

        elif opcao == "2":
            numero_contas, numero_agencia = criar_conta(
                usuarios,
                contas,
                numero_contas=numero_contas,
                numero_agencia=numero_agencia
            )

        elif opcao == "3":
            filtrar_usuario(usuarios, contas)
        
        elif opcao == "4":
            listar_contas(contas)

        elif opcao == "q":
            print(sistema_exit)
            return exit(0)

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()