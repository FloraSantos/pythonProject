from time import sleep
brasileirao = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print('{:^60}'.format('CAMPEONATO BRASILEIRO 2019'))
while True:
    print('''[A] Os 5 primeiros colocados
             [B] Os ultimos 4 colocados
             [C] Lista com os times em ordem alfabetica
             [D] Em que posição está o time da chapecoence
             [E] sair''')
    opc = str(input('Digite sua opção:')).upper()
    if opc == 'A':
        print(brasileirao[0:5])
    elif opc == 'B':
        print(brasileirao[-4:])
    elif opc == 'C':
        print(sorted(brasileirao))
    elif opc == 'D':
        print('O Chapecoense entá na posição {}.'.format(brasileirao.index('Chapecoense')+1))
    elif opc == 'E':
        print('Saindo...')
        sleep(2)
        print('Programa finalizado!')
        break


#print(f'{"LISTAGEM":^40}')

#print(*names, sep=", ")