num = int(input('Digite um numero inteiro: '))
print()

print('-' * 20)
print('[ 1 ] para Binário')
print('[ 2 ] para Octadecimal')
print('[ 3 ] para Hexadecimal')
print('-' * 20)
base = int(input('Informe a base de conversão: '))

if base == 1:
    print('{} em Binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} em Octadecimal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} em Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
