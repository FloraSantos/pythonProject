n1 = list()
n2 = list()
for c in range(3):
    n1.append(input('Digite seu nome:'))
    n1.append(int(input('Digite sua idade:')))
    n2.append(n1[:])
    n1.clear()

for v in n2:
    if v[1] <= 21:
        if v[1] == 1:
            print(f'{v[0]} está dentro do pradão exigido! {v[1]} ano')
        else:
            print(f'{v[0]} está dentro do pradão exigido! {v[1]} anos')
    else:
        if v[1] == 1:
            print(f'{v[0]} passou do padrão! {v[1]} ano')

print(n2)