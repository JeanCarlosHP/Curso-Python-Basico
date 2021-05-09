from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
    if inicio < fim:
        for parametro in range(inicio, fim + 1, passo):
            print(parametro, end=' ')
            sleep(0.5)
    else:
        for parametro in range(inicio, fim - 1, -passo):
            print(parametro, end=' ')
            sleep(0.5)
    print('FIM!')
    print('-=-' * 15)


print('-=-' * 15)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio_var = int(input('Inicio: '))
fim_var = int(input('Fim: '))
passo_var = int(input('Passo: '))
print('-=-' * 15)
contador(inicio_var, fim_var, passo_var)
