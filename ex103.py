def fun(nome, gols):
    if nome in '':
        nome = '<Desconhecido>'

    if gols in '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


j = input('Nome do Jogador: ').capitalize()
g = input('Número de gols: ')
fun(j, g)