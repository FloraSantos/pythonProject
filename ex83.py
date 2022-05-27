exp = list((input('Digite a expressão: ')).strip())
if exp.count('(') == exp.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')