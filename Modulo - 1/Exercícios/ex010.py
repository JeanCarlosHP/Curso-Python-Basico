real = float(input('\033[33mQuantos reais você tem na carteira? R$'))
print()

dolar = real / 3.27

print('\033[33mVocê pode comprar \033[31m${:.2f}\033[m \033[33mdolares!'.format(dolar))
