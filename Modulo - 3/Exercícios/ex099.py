from time import sleep


def maior(* valores):
    maior_valor = 0
    print('-=-' * 15)
    print('Analizando os valores passados...')
    for valor in valores:
        print(valor, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(valores)} valores ao todo.')
    for valor in valores:
        if valor > maior_valor:
            maior_valor = valor
    print(f'O maior valor informado foi {maior_valor}.')
    print('-=-' * 15)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
