palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'TRABALHAR')
for c in palavras:
    print(f'\nNas palavras {c} temos', end=' ')
    for vogais in c:
        if vogais.lower() in 'aeiou':
            print(vogais, end='  ')
