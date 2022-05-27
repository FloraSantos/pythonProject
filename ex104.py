def leiaInt(numero):
    while True:
        numero = str(input(numero))
        if numero.isnumeric():
            return numero
        else:
            print('\033[31m Erro. Digite outro número. \033[m')
        break


numero = leiaInt('Digite um número: \033[36m')
print(f'\n\033[32mO número digitado foi:\033[m \033[33m{numero} \033[m')
