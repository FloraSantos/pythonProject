dic = dict()
dic["nome"] = str(input("Nome do aluno : "))
dic["média"] = float(input(f'Media de {dic["nome"]} : '))
print(f'O aluno {dic["nome"]} tem média igual a {dic["média"]} ')
if dic["média"] >= 7 :
    print(f'O aluno {dic["nome"]} foi APROVADO !!!')
else :
    print(f'O aluno {dic["nome"]} foi REPROVADO !!!')




