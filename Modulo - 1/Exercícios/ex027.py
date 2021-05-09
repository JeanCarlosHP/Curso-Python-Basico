nome = input('Digite seu nome completo: ').strip()

nome = nome.title()
lista = nome.split()

print('Primeiro nome: {}'.format(lista[0]))
print('Ultimo nome: {}'.format(lista[-1]))
