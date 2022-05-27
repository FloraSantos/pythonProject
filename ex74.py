from random import randint
cont = 0
lista2 = []
computador = randint(0,20)
comp2 = randint(0,10)
comp3 = randint(0,30)
comp4 = randint(0,60)
comp5 = randint(0,80)
lista = (computador,comp2,comp3,comp4,comp5)
lista2 += [lista[0]]
for cont in range(1):
    print(lista)
print('O maior número é o {} e o menor número é {}'.format(max(lista), min(lista)))






