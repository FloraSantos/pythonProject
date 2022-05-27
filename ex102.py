def fatorial(num, show=False):
    f = 1
    if show == True:
        for c in range(num, 1, -1):
            f *= c
            print(f'{c} X ', end='')
        print(f'1 = ', end='')
        return f
    if show == False:
        for c in range(num, 1, -1):
            f *= c
        return f'O fatorial de {num} é igual a {f}'


#programa principal
num = int(input('Digite o número que quer o calculo fatorial? '))
detalhe = input('Deseja resultado detalhado (Sim / Não)? ').upper()[0]
while detalhe not in 'SN':
    detalhe = input('Deseja detalhado (Sim / Não)? ').upper()[0]
if detalhe in 'Ss':
    detalhe = True
else:
    detalhe = False
print(fatorial(num, detalhe))