def leiaint(mensagem):
    print('--' * 20)
    global numero
    certo = False
    valor = 0
    while True:
        numero = str(input(mensagem)).strip()
        if numero.isnumeric():
            valor = int(numero)
            certo = True
        else:
            print('ERRO! Digite um numero inteiro valido.')
        if certo:
            break
    return valor


numero = leiaint('Digite um numero: ')
print('--' * 20)
print(f'Voce acabou de digitar o numero {numero}')
