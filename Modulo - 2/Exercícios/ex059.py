valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
opcao = 0

while opcao != 5:
    print('-' * 21)
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do programa''')
    print('-' * 21)
    opcao = int(input('Informe a opção: '))
    print()

    if opcao == 1:
        soma = valor1 + valor2
        print('A soma entre {} e {} é igual a {}'.format(valor1, valor2, soma))
    elif opcao == 2:
        mult = valor1 * valor2
        print('A multiplicação entre {} e {} é igual a {}'.format(valor1, valor2, mult))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior numero é o {}'.format(maior))
    elif opcao == 4:
        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Voce saiu do programa!')
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
    print('-=-' * 20)
