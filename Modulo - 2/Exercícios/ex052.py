n = int(input('Digite um numero: '))

if n == 2:
    print('É um numero primo!')
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print('Não é um numero primo!')
else:
    print('É um numero primo!')
