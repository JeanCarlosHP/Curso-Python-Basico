def area(largura, comprimento):
    area_do_terreno = largura * comprimento
    print(f'A area de um terreno {largura}x{comprimento} é de {area_do_terreno}m².')


print('-' * 30)
print('Controle de Terrenos')
print('-' * 30)
area(float(input('LARGURA(m): ')), float(input('COMPRIMENTO(m): ')))
