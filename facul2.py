code = 0       # Recebe as escolhas do cárdapio
valor = 0      # Recebe os preços
soma = 0       # Recebe a soma dos pedidos
id = 'Bem vindo a Loja da FLORA SANTOS RIBEIRO SILVA RU:3922190'
print(id)      # indentificador pessoal
print('**********************Cardapio*****************')
print('''Código	           Descrição	          Valor(R$)
    |100|	     Cachorro-Quente	       |9,00|
    |101|	     Cachorro-Quente Duplo	   |11,00|
    |102|	     X-Egg	                   |12,00|
    |103|	     X-Salada	               |13,00|
    |104|	     X-Bacon	               |14,00|
    |105|	     X-Tudo	                   |17,00|
    |200|	     Refrigerante Lata	       |5,00|
    |201|	     Chá Gelado	               |4,00|
    ''')
while True:                                             #Estrutura de repetição
    cod = int(input('Entre com o código desejado:'))
    if cod == 100:
        code = "Cachorro quente"
        valor = 9.00
        soma += valor
        print('Você pediu um {} no valor de R$ {}'.format(code, valor))
        print()
    elif cod == 101:
        code = 'Cachorro-Quente Duplo'
        valor = 11.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    elif cod == 102:
        code = 'X-Egg'
        valor = 12.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    elif cod == 103:
        code = 'X-Salada'
        valor = 13.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    elif cod == 104:
        code = 'X-Bacon'
        valor = 14.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    elif cod == 105:
        code = 'X-Tudo	'
        valor = 17.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    elif cod == 200:
        code = 'Refrigerante Lata'
        valor = 5.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    elif cod == 201:
        code = 'Chá Gelado'
        valor = 4.00
        soma += valor
        print('Você pediu um {} no valor de R$ {:.2f}'.format(code, valor))
        print()
    else:
        print('Opção inválida!')
        continue                    # Retorna o laço ao início
    des = str(input('Deseja pedir mais alguma coisa (S/N) ?')).upper()
    if des == 'N':
        break                       # Encerra o laço
print('O total a ser pago é: R$ {:.2f}'.format(soma))           # Valor final


