while True:
    tabu = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 33)
    if tabu < 0:
        break
    for cont in range(1, 11):
        print(f'{tabu} x {cont} = {tabu * cont}')
    print('-' * 33)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
