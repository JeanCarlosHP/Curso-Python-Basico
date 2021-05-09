soma = cont = 0
num = int(input('Informe um numero [999 para parar]: '))

while num != 999:
    soma += num
    cont += 1
    num = int(input('Informe um numero [999 para parar]: '))
print('Foram digitados {} numero e a soma entre eles é igual a {}'.format(cont, soma))
