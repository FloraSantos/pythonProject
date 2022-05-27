from random import randint

numeros = list()


def sorteia():
    """ função de sorteio"""
    print('Sorteando os valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append((randint(0, 15)))
    print(f'{numeros} ', end='')
    print('PRONTO!')

def somaPar():
    contPar = 0
    for c in numeros:
        if c % 2 == 0:
            contPar += c
    print(f'Somando os valores pares da lista {numeros} temos {contPar}.')


sorteia()
somaPar()
help(sorteia)