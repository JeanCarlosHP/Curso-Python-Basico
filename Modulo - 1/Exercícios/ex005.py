number = int(input('\033[30;47mDigite um número inteiro:\033[m '))

sucessor = number + 1
antecessor = number - 1

print('O sucessor de \033[33m{}\033[m é: \033[31m{}\033[m'.format(number, sucessor))
print('O antecessor de \033[33m{}\033[m é: \033[31m{}\033[m'.format(number, antecessor))
