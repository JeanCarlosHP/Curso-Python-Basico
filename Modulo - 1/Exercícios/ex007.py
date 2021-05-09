nota1 = float(input('\033[0;30;47mDigite a primeira nota:\033[m '))
nota2 = float(input('\033[0;30;47mDigite a segunda nota:\033[m '))
print()
media = (nota1 + nota2) / 2

print('A media entre \033[32m{:.1f}\033[m e \033[32m{:.1f}\033[m é: \033[33m{:.1f}'.format(nota1, nota2, media))
