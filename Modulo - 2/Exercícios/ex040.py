nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Aprovado!')
elif media >= 5 or media <= 6.9:
    print('Recuperação!')
else:
    print('Reprovado!')
