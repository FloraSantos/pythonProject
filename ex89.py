lista = list()
while True:
    nome = input('Seu nome:')
    nota1 = float(input('NOTA1:'))
    nota2 = float(input('NOTA2:'))
    media = nota1 + nota2 / 2
    lista.append([nome, [nota1, nota2], media])
    perg = input('Quer continuar ?').upper()
    if perg == 'N':
        break

print(f'{"NO":<4}{"NOME":<10}{"MÉDIA":<8}')
for i, aluno in enumerate(lista):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:<8}')

while True:
    print('-' * 25)
    aluno = int(input('Deseja ver a nota de qual aluno? (999 para parar) '))
    if aluno == 999:
        break
    else:
        print(f'As notas de {lista[aluno][0]} são {lista[aluno][1]}')
print('Programa Finalizado\nVolte sempre! :D')
