cores = {'corTexto': '\033[30;47m',
         'Red': '\033[31m',
         'Yellow': '\033[33m',
         'Limpa': '\033[m'}

num = int(input('{}Digite um número:{} '.format(cores['corTexto'], cores['Limpa'])))
print()

print('-' * 12)
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 1, cores['Limpa'], cores['Red'],num * 1, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 2, cores['Limpa'], cores['Red'],num * 2, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 3, cores['Limpa'], cores['Red'],num * 3, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 4, cores['Limpa'], cores['Red'],num * 4, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 5, cores['Limpa'], cores['Red'],num * 5, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 6, cores['Limpa'], cores['Red'],num * 6, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 7, cores['Limpa'], cores['Red'],num * 7, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 8, cores['Limpa'], cores['Red'],num * 8, cores['Limpa']))
print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 9, cores['Limpa'], cores['Red'],num * 9, cores['Limpa']))
print('{}{}{} x {}{}{} = {}{}{}'.format(cores['Yellow'], num, cores['Limpa'], cores['Yellow'], 10, cores['Limpa'], cores['Red'],num * 10, cores['Limpa']))
print('-' * 12)
