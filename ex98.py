from time import sleep


def contar(a, b, c):
    if c == 0 or a == b:
        c = 1
    if (a - b > 0 and c > 0) or (a - b < 0 and c < 0):
        c *= -1
    print('=-' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if a > b:
        b -= 1
    elif b > a:
        b += 1
    for x in range(a, b, c):
        sleep(0.5)
        print(f'{x} ', end='')
    sleep(0.5)
    print('FIM')