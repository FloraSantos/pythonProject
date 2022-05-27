
indentificador = "FLORA SANTOS RIBEIRO SILVA RU:3922190"  # Identificador pessoal
print()
pecasCadastradas = {}             # Dicionário para guardar os dados das peças
print()
def Cadastrarpecas(j):               # Função para realizar o cadastro
    print("Código da Peça: {}".format(j))         # Imprime na tela o código da peça
    nomeDpeca = input("Entre com o NOME da peça: ")   # Recebe o nome da peça adicionada
    fPeca = input("Entre com o FABRICANTE da peça: ")   # Recebe o nome do fabricante
    valordPeca = float(input("Entre com o VALOR da peça: "))  # Recebe o valor em R$ da peça
    pecasCadastradas[j] = [j, nomeDpeca, fPeca,valordPeca]  # Adiciona os dados das peças no dicionário


def consultarPeca():                   # Função para consultar as peças
    print("Escolha a opção desejada:")
    print("1. Consultar todas as peças")
    print("2. Consultar peças por código")
    print("3. Consultar peças por fabricante")
    print("4. Retornar")
    escolha = int(input('->'))         # Recebe a escolha do usuário de 1 até o 4
    if escolha == 1:                   # Verificação da escolha
        for dados in pecasCadastradas.values():  # Para percorrer todos os valores do dicionário
            print(
                "Código: {} \nNome: {} \nFabricante: {} \nValor: {:.2f}".format(dados[0], dados[1], dados[2], dados[3]))
            print("------------------------------")
    elif escolha == 2:
        codigoI = int(input("Digite o CÓDIGO da peça: "))  # Recebe o código digitado pelo usuário
        print()
        for dados in pecasCadastradas.values():
            if codigoI == dados[0]:   # Condição para imprimir na tela apenas a peça correspondente ao código digitado
                print("Código: {} \nNome: {} \nFabricante: {} \nValor: {:.2f}".format(dados[0], dados[1], dados[2],dados[3]))
                print("------------------------------")
    elif escolha == 3:
        fabIinput = input("Digite o FABRICANTE da peça: ")  # Recebe o nome do fabricante digitado
        print()
        for dados in pecasCadastradas.values():
            if fabIinput == dados[2]:    # Condição para imprimir na tela apenas as peças correspondentes ao fabricante digitado
                print("Código: {} \nNome: {} \nFabricante: {} \nValor: {:.2f}".format(dados[0], dados[1], dados[2], dados[3]))
                print("------------------------------")
    elif escolha == 4:
        pass      # Para voltar ao loop
    else:
        print("Opção inválida!")
        pass


def remover():
    codigoR = int(input("Digite o código da peça a ser removida: "))  # Recebe o código digitado
    del pecasCadastradas[codigoR]  # Remove do dicionário o item (chave + valor) correspondente ao código digitado


print("Bem Vindo ao Controle de Estoque da Bibicletaria da {}".format(indentificador))

codigo = 1  # Primeiro valor para o código da primeira peça a ser cadastrada
while True:
    print("Escolha a opção desejada:")
    print("1. Cadastrar Peça")
    print("2. Consultar Peça")
    print("3. Remover Peça")
    print("4. Sair")
    esc = int(input('-> '))        # Escolha digitada pelo usuário
    if esc == 1:                   # Verifica a escolha do usuário
        print("Você selecionou a opção de Cadastrar Peças")
        Cadastrarpecas(codigo)     # Execução da função para cadastrar as peças (parâmetro do valor atual)
        codigo += 1
    elif esc == 2:
        print("Você selecionou a opção de Consultar Peças")
        consultarPeca()            # função de consultar peças, o usuário deve escolher 1 dentre as  4 opções
    elif esc == 3:
        print("Você selecionou a opção de Remover Peças")
        remover()                  # Execução da função de remover peças
    elif esc == 4:                 # Opção para sair
        break
    else:                          # Utilizada para quando o usuário digitar um valor diferente
        print("Opção inválida!")
        continue                   # Leva ao início do loop