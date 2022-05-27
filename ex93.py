lista = list()
lista2 = list()
soma = 0
count = 0
dicio = dict()
dicio['Nome'] = input('Nome:')
dicio['Partidas'] = int(input(f'Quantas partidas {dicio["Nome"]} jogou ?'))
for c in range(1, dicio['Partidas'] + 1):
    dicio['Gols'] = int(input(f'Quantos gols na partida {c} ?'))
    soma += dicio['Gols']
    lista.append(dicio['Gols'])
    dicio['Gols'] = lista
    dicio['Total'] = soma
    lista2.append(dicio['Gols'])
print(dicio)
print('='*40)
print(f'O campo nome tem o valor {dicio["Nome"]}')
print(f'O campo gols tem o valor {dicio["Gols"]}')
print(f'O campo total tem o valor {dicio["Total"]}')
print('='*40)
print(f'O jogador {dicio["Nome"]} jogou {dicio["Partidas"]} partidas!.')
for i, c in enumerate(lista2):
    print(f'Na partida {i+1}, fez {c[i]} gols!')






