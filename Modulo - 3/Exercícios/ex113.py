def mostraLinha(tipo='-', tamanho=1):
    print(tipo * tamanho)


def leiaInt(mensagem):
    mostraLinha('-', 40)
    global numero_inteiro
    while True:
        try:
            numero_inteiro = str(input(mensagem)).strip().replace(',', '.')
            if numero_inteiro == '':
                print('Usuário preferiu não digitar esse número.')
                numero_inteiro = 0
            else:
                numero_inteiro = int(numero_inteiro)
        except ValueError:
            print('ERRO! Por favor, digite um número inteiro válido.')
        else:
            break
    return numero_inteiro


def leiaFloat(mensagem):
    mostraLinha('-', 40)
    global numero_real
    while True:
        try:
            numero_real = str(input(mensagem)).strip().replace(',', '.')
            if numero_real == '':
                print('Usuário preferiu não digitar esse número.')
                numero_real = 0
            else:
                numero_real = float(numero_real)
        except ValueError:
            print('ERRO! Por favor, digite um número real válido.')
        else:
            break
    return numero_real


numero_inteiro = leiaInt('Digite um número inteiro: ')
numero_real = leiaFloat('Digite um número real: ')
mostraLinha('-=', 20)
print(f'O valor inteiro digitado foi {numero_inteiro} e o real foi {numero_real}')
