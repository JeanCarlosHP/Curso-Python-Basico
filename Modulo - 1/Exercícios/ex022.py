nome = input('Digite seu nome: ')

lista = nome.split()
print('Todas as letras maiusculas: ', nome.upper())
print('Todas as letras minusculas: ', nome.lower())
print('Quantas letras ao todo(sem considerar os espaços): ', len(''.join(nome.split())))
print('Quantas letras tem só o primeiro nome: ', len(lista[0]))
