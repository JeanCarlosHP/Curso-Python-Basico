num = int(input('Digite um numero inteiro: '))
cont = num
f = 1

print('Calculando {}! = '.format(num), end='')

while cont > 0:
    print('{}'.format(cont), end='')
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= cont
    cont -= 1
print('{}'.format(f))

# num = int(input('Digite um numero inteiro: '))
# f = 1
# for c in range(0, num):
#     print('{}'.format(num), end='')
#     if num > 1:
#         print(' x ', end='')
#     else:
#         print(' = ', end='')
#     f *= num
#     num -= 1
# print('{}'.format(f))
