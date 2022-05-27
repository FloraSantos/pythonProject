matriz = [[], [], []]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha},{coluna}]: ')))
for linha in matriz:
    print(linha)
