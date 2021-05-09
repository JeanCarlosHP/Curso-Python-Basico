mediaIdade = 0
nomeMaisVelho = ''
idadeMaisVelho = 0
mulheres = 0

for i in range(1, 5):
    print('DADOS DA {}° PESSOA!'.format(i))
    nome = input('Informe o nome da pessoa: ')
    idade = int(input('Informe a idade da pessoa: '))
    sexo = input('Informe o sexo da pessoa: ').lower()

    mediaIdade = mediaIdade + idade
    if sexo == 'masculino':
        if idade > idadeMaisVelho:
            nomeMaisVelho = str(nome)
    if sexo == 'feminino':
        if idade < 20:
            mulheres += 1
    print()
    print('-' * 20)
    print()

print()
print('-' * 20)
print('A média de idade do grupo é: {}'.format(mediaIdade / 4))
print("O homem mais velho tem {} anos e se chama {}".format(idadeMaisVelho, nomeMaisVelho))
print('Tem {} mulheres com menos de 20 anos'.format(mulheres))
print('-' * 20)
