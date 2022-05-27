n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = ((n1, n2, n3, n4))
print(f'Os valores digitados foram {valores}')
print(f'Quantidade de 9 que apareceram {valores.count(9)}')
if 3 in valores:
    print(f'Posição do número 3 é {valores.index(3)+1}')
else:
    print(f'O valor 3 não foi achado em nenhuma posição!')
for c in valores:
    if c % 2 == 0:
        print(f' números pares digitados {c}')



