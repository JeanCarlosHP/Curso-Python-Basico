cores = {'corTexto': '\033[0;30;47m',
         'Amarelo': '\033[33m',
         'Limpa': '\033[m',
         'Verde': '\033[32m'}

number = int(input('{}Digite um número:{} '.format(cores['corTexto'], cores['Limpa'])))
print()

dobro = number * 2
triplo = number * 3
raizQuadrada = number ** 0.5

print('{}O dobro de {}{}{}{} é:{} {}{}{}'.format(cores['corTexto'], cores['Amarelo'], number, cores['Limpa'], cores['corTexto'], cores['Limpa'], cores['Verde'], dobro, cores['Limpa']))
print('{}O triplo de {}{}{}{} é :{} {}{}{}'.format(cores['corTexto'], cores['Amarelo'], number, cores['Limpa'], cores['corTexto'], cores['Limpa'], cores['Verde'], triplo, cores['Limpa']))
print('{}A raiz quadrada de {}{}{}{} é:{} {}{:.2f}{}'.format(cores['corTexto'], cores['Amarelo'], number, cores['Limpa'], cores['corTexto'], cores['Limpa'], cores['Verde'], raizQuadrada, cores['Limpa']))
