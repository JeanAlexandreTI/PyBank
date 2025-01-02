# **Projeto: Sistema Bancário Simples em Python**

# **Objetivo:** Criar um sistema bancário simples onde o usuário possa realizar operações como depósito, saque, transferência entre contas e consulta de saldo. Este projeto tem como objetivo proporcionar uma introdução ao desenvolvimento de sistemas em Python, trabalhando com funções, controle de fluxo, manipulação de dados e, de forma opcional, persistência de dados utilizando arquivos simples.

# ---

# ### Funcionalidades Requeridas:

# 1. **Cadastro de Conta**:
#    - O sistema deve permitir a criação de uma conta bancária. Cada conta deve ter:
#      - Nome do titular.
#      - Número da conta (um identificador único).
#      - Saldo inicial (inicialmente 0,00).
#      - Um código de acesso (senha) para operações sensíveis, como saque e transferência.

# 2. **Depósito**:
#    - O usuário deve poder realizar depósitos em sua conta. 
#    - O sistema deve permitir depósitos de valores positivos (ex: R$ 100,00).
#    - O saldo da conta deve ser atualizado corretamente após o depósito.

# 3. **Saque**:
#    - O usuário deve poder sacar valores da sua conta.
#    - O sistema deve validar que o saldo da conta é suficiente para cobrir o saque solicitado.
#    - O valor mínimo de saque será de R$ 10,00.
#    - Caso o saldo seja insuficiente ou o valor do saque seja menor que o mínimo, uma mensagem de erro deve ser exibida.

# 4. **Transferência**:
#    - O sistema deve permitir transferências entre contas.
#    - Para realizar a transferência, o usuário deve informar o número da conta de destino, o valor a ser transferido e, se necessário, a senha da conta.
#    - O valor da transferência deve ser descontado da conta de origem e adicionado à conta de destino.
#    - O sistema deve validar que o valor da transferência não ultrapassa o saldo da conta de origem e que o valor mínimo de transferência é de R$ 10,00.

# 5. **Consulta de Saldo**:
#    - O usuário deve poder consultar o saldo da sua conta a qualquer momento.
#    - O saldo deve ser exibido com a formatação correta (ex: R$ 100,00).

# 6. **Exibição de Histórico de Transações** (opcional):
#    - O sistema pode manter um histórico simples de transações realizadas (depósitos, saques, transferências) para cada conta.
#    - Este histórico pode ser armazenado em uma lista ou arquivo de texto (dependendo do seu progresso).

# ### Estrutura do Projeto:

# 1. **Classes e Funções**:
#    - O projeto pode ser estruturado utilizando **classes** para representar as contas bancárias. 
#      - A classe `ContaBancaria` pode conter atributos como `nome`, `numero_conta`, `saldo`, `senha`, e métodos para realizar as operações (depósito, saque, transferência, consulta de saldo).
#    - Para cada funcionalidade (depósito, saque, etc.), você pode criar **funções** dentro da classe ou funções separadas fora da classe.

# 2. **Interação com o Usuário**:
#    - O sistema pode ser operado em um menu interativo no terminal, onde o usuário escolhe a opção desejada (ex: "1. Depositar", "2. Sacar", "3. Transferir", "4. Ver Saldo", etc.).
#    - As opções devem ser exibidas em um loop até que o usuário escolha a opção de sair.

# 3. **Validação de Entrada**:
#    - O sistema deve ser capaz de lidar com entradas inválidas, como números negativos, letras quando se espera números, ou valores fora do limite.
#    - Certifique-se de verificar que a senha informada para as transações (como saque e transferência) seja correta.

# ### Sugestões para o Desenvolvimento:

# 1. **Estrutura de Dados**:
#    - Utilize um **dicionário** para armazenar as contas bancárias, onde o número da conta será a chave e a instância da classe `ContaBancaria` será o valor.
   
# 2. **Validações**:
#    - Ao realizar transferências, verifique se o número da conta de destino existe.
#    - Quando o usuário fizer um saque ou transferência, verifique se ele tem saldo suficiente e se o valor é válido.

# 3. **Armazenamento de Dados** (opcional):
#    - Se quiser, pode armazenar as contas bancárias e seus saldos em um arquivo de texto (como um arquivo CSV ou JSON) para persistência entre execuções do programa.
#    - Caso opte por não usar persistência, todos os dados serão perdidos quando o programa for fechado.

# 4. **Frameworks (para funcionalidades específicas)**:
#    - **Argparse**: Caso queira melhorar a interação via linha de comando, pode usar o módulo `argparse` para aceitar argumentos diretamente no terminal, como número da conta e valores para depósito ou saque.
#    - **SQLite**: Caso queira persistir dados em um banco de dados simples, pode usar o módulo `sqlite3` para armazenar as contas bancárias e transações em um banco de dados local.
   
# ---

# ### Como Executar:

# 1. **Criação da Conta Bancária**:
#    - O sistema solicitará o nome do titular e gerará automaticamente o número da conta e o saldo inicial de 0,00.
   
# 2. **Menu de Opções**:
#    - Após a criação da conta, o usuário será apresentado com um menu de opções:
#      - **1**: Depositar
#      - **2**: Sacar
#      - **3**: Transferir
#      - **4**: Ver Saldo
#      - **5**: Sair

# 3. **Operações**:
#    - Quando o usuário escolhe uma operação, ele será solicitado a inserir os dados necessários (valor de depósito, valor de saque, número da conta de destino, etc.).
#    - Após a operação, o menu será exibido novamente até que o usuário escolha a opção de sair.

# 4. **Saída**:
#    - Quando o usuário escolher sair, o programa deve exibir uma mensagem de despedida e encerrar a execução.

# ---

# ### Dicas Adicionais:

# - Teste cada funcionalidade individualmente para garantir que o sistema funcione corretamente.
# - Mantenha o código bem organizado e use comentários para explicar as partes mais importantes do código.
# - Após concluir o básico, você pode tentar adicionar novas funcionalidades, como a opção de exibir o histórico de transações ou implementar taxas de transação.

# Este projeto é uma ótima maneira de aprender mais sobre estruturas de dados, lógica de programação e interação com o usuário em Python.




# =======================================================================================================================================================================================



# CRIAÇÃO DA CONTA USUÁRIO
print("Para realizar a criação de uma conta bancaria, precisamos que forneça os dados a baixo:")

user = ''
loginUser = ''
saldo = 0

while True:
    try:
        nomeTitular = input('Nome do Titular da conta: ').title().strip()
        senhaTitular = input('Crie uma senha contendo números inteiros (4 digitos): ')

        if nomeTitular.isalpha() == False:
            print("Seu nome deve ser composto por apenas letras!")
            print('Peço que informe os dados solicitados corretamente.')    
        
        elif senhaTitular.isdigit() == False or len(senhaTitular) != 4:
            print("Sua senha deve conter apenas números e ter 4 digitos!")
            print("Peço que informe os dados solicitados corretamente.")

        elif len(senhaTitular) == 4:
            confirmaSenha = input("Confirme sua senha: ")

            if confirmaSenha == senhaTitular:
                print("Senha confirmada e conta criada!")
                user = nomeTitular
                loginUser = senhaTitular
                break
            else:
                print("As senhas devem ser iguais!")
                print("Informe os dados novamente:")

    except (TypeError, ValueError):
        print("Tipo de dado incorreto.", end = " ")
        print("Peço que informe os dados solicitados corretamente.")
    except Exception as error:
        print(f'Ocorreu um erro do tipo {error.__class__}')

# REALIZAÇÃO DE DEPOSITO, SAQUE E TRANSFERENCIAS

while True:
    menu = int(input('''Escolha dentre as opções: 
    - [1]: Depositar
    - [2]: Sacar
    - [3]: Transferir
    - [4]: Ver Saldo
    - [5]: Sair
    Informe a opção desejada: '''))

    if menu == 1:

        while True:
            
            try:
                print('Insira o valor do seu deposito: ')
                deposito = float(input('R$: '))
                
                if deposito > 0: 
                    
                    
                    senha = input('Insira sua senha para realizar o deposito: ')
                    
                    if senha == loginUser:
                        saldo += deposito

                        print(f"Valor de R${deposito} depositado. Saldo atual da sua conta é de R${saldo}")
                        break
                    elif senha != loginUser:
                        repeteSenha = 0
                        repeteSenha += 1
                        print('Senha incorreta!')

                        if repeteSenha == 2:
                            recriarSenha = input('Esqueceu sua senha? Deseja criar outra senha? Digite [Sim/Não]: ').title().strip()

                            while True:
                                if recriarSenha == 'Sim':
                                    informUser = input('Informe o nome do Titular da conta bancaria: ').title()

                                    confirmUser = informUser == user

                                    if confirmUser == True:
                                        newLogin = input('Insira a sua nova senha: ')

                                        if newLogin == loginUser:
                                            print('Nova senha não pode ser identica a anterior.', end = ' ')
                                            print('Tente novamente.')

                                        elif newLogin.isdigit() == False or len(newLogin) != 4:
                                            print('Sua senha deve conter apenas números e conter 4 digitos!')

                                        elif newLogin != loginUser:
                                            confirmaSenha = input('Confirme a sua senha: ')

                                            if newLogin == confirmaSenha:
                                                loginUser = newLogin
                                                repeteSenha = 0
                                                print('Nova senha criada!')
                                                break

                                            elif newLogin != confirmaSenha:
                                                print('As senhas devem ser identicas.')

                                elif recriarSenha == 'Não' or recriarSenha == 'Nao':
                                    print('Redefinição de senha recusada.', end=' ')
                                    print('Informe os dados solicitados corretamente.')
                                    repeteSenha = 0       
                                    break

                else:
                    print('Deposite um valor superior a R$0.00')
                
            except (ValueError):
                print('Dados incorretos. Informe-os novamente: ')
            except AttributeError:
                print('Insira o atributo correto.')
            except Exception as error:
                print(f'Tivemos um erro. A classe do erro encontrado é {error.__class__}')
    
    elif menu == 2:
        while True:
            if saldo == 0:
                print('Você não pode efetuar o saque sem possuir um saldo positivo.')
                break
            try:        
                print('Informe o valor que deseja sacar: ')
                saque = float(input('R$: '))
                if saque > saldo:
                    print('Você não pode ficar com valores negativos após o saque.')
                    break

                senha = input('Insira sua senha para realizar o saque: ')

                if senha == loginUser:
                    saldo -= saque

                    print(f"Valor de R${saque} sacado. Saldo atual da sua conta é de R${saldo}")
                    break
                elif senha != loginUser:
                    repeteSenha = 0
                    repeteSenha += 1
                    print('Senha incorreta!')

                    if repeteSenha == 2:
                        recriarSenha = input('Esqueceu sua senha? Deseja criar outra senha? Digite [Sim/Não]: ').title().strip()

                        while True:
                            if recriarSenha == 'Sim':
                                informUser = input('Informe o nome do Titular da conta bancaria: ').title()

                                confirmUser = informUser == user

                                if confirmUser == True:
                                    newLogin = input('Insira a sua nova senha: ')

                                    if newLogin == loginUser:
                                        print('Nova senha não pode ser identica a anterior.', end = ' ')
                                        print('Tente novamente.')

                                    elif newLogin.isdigit() == False or len(newLogin) != 4:
                                        print('Sua senha deve conter apenas números e conter 4 digitos!')

                                    elif newLogin != loginUser:
                                        confirmaSenha = input('Confirme a sua senha: ')

                                        if newLogin == confirmaSenha:
                                            loginUser = newLogin
                                            repeteSenha = 0
                                            print('Nova senha criada!')
                                            break

                                        elif newLogin != confirmaSenha:
                                            print('As senhas devem ser identicas.')

                            elif recriarSenha == 'Não' or recriarSenha == 'Nao':
                                print('Redefinição de senha recusada.', end=' ')
                                print('Informe os dados solicitados corretamente.')
                                repeteSenha = 0       
                                break

                    else:
                        print('Tente novamente.')
            
            except (ValueError):
                print('Dados incorretos. Informe-os novamente: ')
            except AttributeError:
                print('Insira o atributo correto.')
            except Exception as error:
                print(f'Tivemos um erro. A classe do erro encontrado é {error.__class__}')
    
    elif menu == 3:
        while True:
            if saldo == 0:
                print(f'Saldo indisponível para transferencia. Saldo atual: R${saldo}')
                break
            
            try:
                print('Informe o valor que deseja realizar a transferencia.')
                transferencia = float(input('R$: '))

                if transferencia > saldo:
                    print('Você não possui saldo suficiente para completar a transação.')
                    break
                elif transferencia < 10:
                    print('Você não pode tranferir valores inferiores a R$10.00')
                    break
                elif transferencia < saldo and transferencia >= 10:
                    contaDestinoTransferencia = input(f'Informe o número da conta para transferir o valor de R${transferencia}: ')
                    
                    if contaDestinoTransferencia.isdigit() == False or len(contaDestinoTransferencia) != 5:
                        print('O número da conta deve conter apenas números de ter 5 digitos.')
                    elif contaDestinoTransferencia.isdigit() and len(contaDestinoTransferencia) == 5:
                        print(f'A conta que recebera o valor de R${transferencia} possui o número {contaDestinoTransferencia}.')
                        confirmaDestino = input('Digite [Sim] para confirmar esta conta ou [Não] para corrigir.').title()

                        if confirmaDestino == 'Sim':
                            senha = input('Insira sua senha para realizar a transação: ')

                            if senha == loginUser:
                                saldo -= transferencia

                                print(f"Valor de R${transferencia} foi transferido para a conta {contaDestinoTransferencia}. Saldo atual é de R${saldo}")
                                break
                            elif senha != loginUser:
                                repeteSenha = 0
                                repeteSenha += 1
                                print('Senha incorreta!')

                                if repeteSenha == 2:
                                    recriarSenha = input('Esqueceu sua senha? Deseja criar outra senha? Digite [Sim/Não]: ').title().strip()

                                    while True:
                                        if recriarSenha == 'Sim':
                                            informUser = input('Informe o nome do Titular da conta bancaria: ').title()

                                            confirmUser = informUser == user

                                            if confirmUser == True:
                                                newLogin = input('Insira a sua nova senha: ')

                                                if newLogin == loginUser:
                                                    print('Nova senha não pode ser identica a anterior.', end = ' ')
                                                    print('Tente novamente.')

                                                elif newLogin.isdigit() == False or len(newLogin) != 4:
                                                    print('Sua senha deve conter apenas números e conter 4 digitos!')

                                                elif newLogin != loginUser:
                                                    confirmaSenha = input('Confirme a sua senha: ')

                                                    if newLogin == confirmaSenha:
                                                        loginUser = newLogin
                                                        repeteSenha = 0
                                                        print('Nova senha criada!')
                                                        break

                                                    elif newLogin != confirmaSenha:
                                                        print('As senhas devem ser identicas.')

                                        elif recriarSenha == 'Não' or recriarSenha == 'Nao':
                                            print('Redefinição de senha recusada.', end=' ')
                                            print('Informe os dados solicitados corretamente.')
                                            repeteSenha = 0       
                                            break

                                else:
                                    print('Tente novamente.')
                        elif confirmaDestino == 'Não' or confirmaDestino == 'Nao':
                            print('Por favor, informe o valor de transferencia novamente.')
                            print('Informe de forma correta a conta destinada a receber o valor de transação desejado.')


            except (ValueError):
                print('Dados incorretos. Informe-os novamente: ')
            except AttributeError:
                print('Insira o atributo correto.')
            except Exception as error:
                print(f'Tivemos um erro. A classe do erro encontrado é {error.__class__}')

    elif menu == 4:
        print(f'Saldo disponível: R${saldo}')
        print('Qual ação deseja tomar?')
    elif menu == 5:
        confirmSair = input('Encerrar sistema?').title()
        
        if confirmSair == 'Sim':
            print('Programa encerrado.')
            print('Obrigado por confiar na Pybank!')
            break
        elif confirmSair == 'Não' or confirmSair == 'Nao':
            print('Qual ação deseja tomar?')
            