from datetime import date
apo = 0
while True:
    dicio = dict()
    dicio['Nome'] = input('Nome:')
    dicio['Ano de nascimento:'] = int(input('Ano de nascimento:'))
    dicio['Sexo'] = input('Sexo (F/M):').upper()
    atual = date.today().year
    idad = atual - dicio['Ano de nascimento:']
    dicio['Idade'] = idad
    dicio['Carteira'] = int(input('Carteira de trabalho (0 não tem):'))
    if dicio['Carteira'] == 0:
        break
    else:
        dicio['ano'] = int(input('Ano de contratação:'))
        dicio['sálario'] = float(input('Sálario:'))
    if dicio['Sexo'] == 'F':
        apo = (dicio['ano'] + 30) - dicio['Ano de nascimento:']
    elif dicio['Sexo'] == 'M':
        apo = (dicio['ano'] + 35) - dicio['Ano de nascimento:']
    conti = input('Quer continuar (M/F) ?').upper()
    if conti == 'N':
        break
print(f'Nome tem o valor {dicio["Nome"]}')
print(f'Contratação tem o valor {dicio["ano"]}')
print(f'CTPS tem o valor {dicio["Carteira"] }')
print(f'Sálario tem o valor {dicio["sálario"] }')
print(f'Você vai se aposentar com {apo}')

