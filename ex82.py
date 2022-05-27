lista = list()
lista2 = list()
lista3 = list()
while True:
        try:
            n1 = int(input('Digite um número:'))
            lista.append(n1)
            if n1 % 2 == 0:
                lista2.append(n1)
            elif n1 % 2 == 1:
                lista3.append(n1)
            n2 = '  '
            while n2 not in 'SN':
                n2 = str(input('Quer continuar(S/N) ?').upper())
            if n2 == 'N':
                break
        except ValueError:
            print('Não aceitamos esse valor!')

print(f'TOTAL: {lista}')
print(f'PARES:{lista2}')
print(f'IMPARES: {lista3}')


