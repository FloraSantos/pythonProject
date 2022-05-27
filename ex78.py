lista = list()
for c in range(5):
    lista.append(int(input('Digite um valor:')))
print(f'Números que foram colocados na lista ', end=' ')
print(*lista, sep=",")
print(f'O maior valor digitado foi {max(lista)} e está na posição {lista.index(max(lista))} \nO menor valor foi {min(lista)} e está na posição {lista.index(min(lista))}')



