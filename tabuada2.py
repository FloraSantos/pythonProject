n2 = 0
s = 0
while True:
        n1 = int(input('Digite um número para ver a tabuada:'))
        for c in range(1,11):
            s = n1 * c
            print(n1, 'x', c, '=', s)
        n2 = ' '
        while n2 not in 'SsNn':
            n2 = str(input('Quer continuar (S/N) ?')).upper().strip()
        if n2 in 'N':
            break

