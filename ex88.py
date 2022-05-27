print('-'*40)
print('JOGA NA MEGA SENA'.center(40))
print('-'*40)
from random import randint
n1 = int(input('Quantos jogos você quer que eu sorteie ?'))
print(f'-----VAMOS SORTEAR {n1} PALPITES-----')
for n1 in range(1, n1 + 1):
    print(f'jogo: {n1}')
    while True:
        lista = list()
        for c in range(0, 6):
            sorte = randint(1, 60)
            lista.append(sorte)

        print(lista)
        break




