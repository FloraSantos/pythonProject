def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    r1 = 'Você ainda não pode votar'
    r2 = 'Para você o voto ainda é opcional'
    r3 = 'Para você o voto é OBRIGATÓRIO'
    r4 = 'Para você o voto é opcional'

    if idade < 16:
        r = r1
        return r
    elif 16 <= idade < 18:
        r = r2
        return r
    elif 18 <= idade < 70:
        r = r3
        return r
    elif idade >= 70:
        r = r4
        return r


m = int(input('Digite o seu ano de nascimento: '))
print(voto(m))
