a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1
termosReserva = 0
termos = 11
while termos != 0:
    termosReserva += termos
    while cont < termosReserva:
        print('{}º Termo = {}'.format(cont, a1))
        a1 += r
        cont += 1
    print()
    print('-=' * 20)
    print()
    termos = int(input('Quer mostar mais termos? Quantos? '))
print('Progressão finalizada com {} termos mostrados'.format(cont - 1))
