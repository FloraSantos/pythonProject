from random import randint
from operator import itemgetter
from time import sleep
jogos = {}
print('Valores sorteados:')
for j in range(1, 5):
    jogos[f'jogador{j}'] = randint(1, 6)
for k, v in jogos.items():
    sleep(1)
    print(f'   O {k} tirou {v}')
podio = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('Ranking dos Jogadores:')
for i, v in enumerate(podio):
    sleep(1)
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')


