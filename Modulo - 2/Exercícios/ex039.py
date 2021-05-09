from datetime import date

ano = int(input('Informe seu ano de nascimento: '))

anoAtual = date.today().year
idade = anoAtual - ano
faltaTempo = idade - 18
passouTempo = (18 - idade) * -1

if idade < 18:
    print('Voce ainda vai se alistar no serviço militar!')
    print('Falta {} ano(s) para voce se alistar!'.format(passouTempo))
elif idade == 18:
    print('Esta na hora de se alistar no serviço militar!')
else:
    print('Ja passou do tempo de se alistar no serviço militar!')
    print('Passou {} ano(s) do tempo do alistamento!'.format(passouTempo))
