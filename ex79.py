lista = list()
while True:
    n = int(input('Digite um número:'))
    if n not in lista:
        lista.append(n)
    else:
        print(f'O número já foi adicionado na lista!')
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Quer continuar (S/N) ?')).upper().strip()
    if conti in 'N':
        break
print(f'Os números adicionados na lista foram: {sorted(lista)}')


