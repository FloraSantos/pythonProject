matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # fiz os teste dentro do primeiro for.
par = terc = maior = 0
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = (int(input(f'Digite um número para [{linha},{coluna}]: ')))
        if matriz[linha][coluna] % 2 == 0:
            par += matriz[linha][coluna]
        if coluna == 2:
            terc += matriz[linha][coluna]
maior = max(matriz[1])
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma dos valores pares digitados é {par}')
print(f'A soma dos valores digitados na 3ª coluna é {terc}')
print(f'O maior valor digitado na 2ª linha é {maior}')
