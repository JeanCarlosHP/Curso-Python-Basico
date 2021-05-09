frase = input('Digite uma frase: ').strip().upper()

print('Aparecem {} "a" na frase.'.format(frase.count('a')))
print('O primeiro "a" aparece na {}º posição.'.format(frase.find('a')+1))
print('O ultimo "a" aparece na {}º posição.'.format(frase.rfind('a')+1))
