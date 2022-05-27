dados = []
povo = []
peso = []
while True:
    dados.append(input('Digite o seu nome:'))
    dados.append(float(input('Digite o seu peso:')))
    povo.append(dados[:])
    peso.append(dados[1])
    dados.clear()
    n1 = ' '
    while n1 not in 'SN':
        n1 = input('Quer continuar (S/N) ?').upper()
    if n1 == 'N':
        break
print(f'Quantidade de pessoas que participaram do cadastro {len(povo)}')
print(f'Pessoa com o maior peso foi: {max(peso)}', end=' ')
for p in povo:
    if p[1] == max(peso):
        print(f'{p[0]}')

print(f'O menor peso foi :{min(peso)}', end=' ')
for p in povo:
    if p[1] == min(peso):
        print(f'{p[0]}')


