desconto = 0       # Vai receber o valor do desconto direto no produto junto a quantidade
desc = 0           # Vai receber o desconto apurado
subtotal = 0
des = 0
id = 'Bem vindo(a) a Loja da FLORA SANTOS RIBEIRO SILVA RU:3922190'
print(id)          # indentificador pessoal
print()            # Espaço para ficar organizado

print('''Quantidades	             Desconto     
Até 9	                 0% na unidade
Entre 10 e 99	         5% na unidade
Entre 100 e 999	         10% na unidade
De 1000 para mais	     15% na unidade''')       # Informações do programa
print()
produto = float(input('Entre com o valor do produto ?'))
quantidade = int(input('Entre com a quantidade ?'))
if quantidade == 9:
    desconto = 0
    subtotal = produto * quantidade
elif (quantidade >= 10) and (quantidade <= 99):
    subtotal = produto * quantidade
    desc = subtotal * (5/100)
    desconto = subtotal - desc
    des = '5%'
elif (quantidade >= 100) and (quantidade <= 999):
    subtotal = produto * quantidade
    desc = subtotal * (10/100)
    desconto = subtotal - desc
    des = '10%'
elif quantidade >= 1000:
    subtotal = produto * quantidade
    desc = subtotal * (15/100)
    desconto = subtotal - desc
    des = '15%'
else:                           # Caso seja digitado um valor inválido
    print('Valor inválido!')

print('O valor sem desconto foi: {:.2f}'.format(subtotal))
print('O valor com desconto foi: {:.2f} (desconto {} )'.format(desconto, des))







