largura = float(input('Digite a lagura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

area = largura * altura
litrosTinta = area / 2

print('A area da parede mede {}m2'.format(area))
print('Voce vai precisar de {}l de tinta'.format(litrosTinta))
