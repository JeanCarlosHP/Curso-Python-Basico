maior = 0
menor = 1000

for i in range(1, 6):
    peso = float(input('Digite o {}° peso: '.format(i)))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

print('O menor peso é {}Kg e o maior peso é {}Kg'.format(menor, maior))
