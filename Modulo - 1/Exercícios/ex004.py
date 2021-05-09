cores = {'Cor': '\033[0;30;47m',
       'Limpa': '\033[m'}

tipoPrimitivo = input('Digite algo: ')

print('O tipo primitivo desse valor é: {}{}{}'.format(cores['Cor'], type(tipoPrimitivo), cores['Limpa']))

print('Só tem espaços? {}{}{}'.format(cores['Cor'], tipoPrimitivo.isspace(), cores['Limpa']))
print('É um número? {}{}{}'.format(cores['Cor'], tipoPrimitivo.isnumeric(), cores['Limpa']))
print('É alfabético? {}{}{}'.format(cores['Cor'], tipoPrimitivo.isalpha(), cores['Limpa']))
print('É alfanémerico? {}{}{}'.format(cores['Cor'], tipoPrimitivo.isalnum(), cores['Limpa']))
print('Esta em maiuscúlas? {}{}{}'.format(cores['Cor'], tipoPrimitivo.isupper(), cores['Limpa']))
print('Esta em minuscúlas? {}{}{}'.format(cores['Cor'], tipoPrimitivo.islower(), cores['Limpa']))
print('Esta capitalizada? {}{}{}'.format(cores['Cor'], tipoPrimitivo.istitle(), cores['Limpa']))
