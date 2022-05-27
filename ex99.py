def maior(*num):
    valores = num
    print(f'{num} foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {max(valores)}')


maior(4, 7, 5, 2)


