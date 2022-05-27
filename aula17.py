tupla = [6,3,7,1,3,4]
tupla.insert(1,1)
tupla.append(10)
tupla.sort(reverse=True)
tupla.pop()
del tupla[4]
tupla.remove(7)
print(*tupla, sep=",")

valores = []
valores.append(4)
valores.append(1)
valores.append(7)
valores.append(9)
for c, v in enumerate(valores):
    print(f'Na posição {c} eu encontrei o valor {v}')



valores = list()
for c in range(5):
    valores.append(int(input('Digite um valor:')))
print('Os valores adicionados foram', end=" ")
print(*valores, sep=",")
print(f'O maior valor foi {max(valores)} e o menor é {min(valores)}')
