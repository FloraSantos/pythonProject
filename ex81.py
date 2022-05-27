lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    if input('Deseja continuar? [S/N] ') in 'Nn':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem descrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')