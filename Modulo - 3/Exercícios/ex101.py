def voto(data_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - data_nascimento
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return print('NÃO VOTA.')
    elif idade >= 65 or 16 <= idade < 18:
        return print('VOTO OPCIONAL.')
    else:
        return print('VOTO OBRIGATÓRIO.')


voto(int(input('Em que ano voce nasceu? ')))
