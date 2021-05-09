m = float(input('\033[30;47mDigite o valor em metros:\033[m '))
print()

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('\033[33mkm:\033[m \033[32m{}\033[m'.format(km))
print('\033[33mhm:\033[m \033[32m{}\033[m'.format(hm))
print('\033[33mdam:\033[m \033[32m{}\033[m'.format(dam))
print('\033[33mdm:\033[m \033[32m{:.0f}\033[m'.format(dm))
print('\033[33mcm:\033[m \033[32m{:.0f}\033[m'.format(cm))
print('\033[33mmm:\033[m \033[32m{:.0f}\033[m'.format(mm))
