cinquenta = vinte = dez = um = 0

print('-=-' * 8)
print('--- CAIXA ELETRONICO ---')
print('-=-' * 8)
print()

saque = int(input('Qual o valor do saque? R$'))
print('===' * 11)
while True:
    if saque == saque:
        cinquenta = int(saque / 50)
        saque -= cinquenta * 50
        vinte = int(saque / 20)
        saque -= vinte * 20
        dez = int(saque / 10)
        saque -= dez * 10
        um = saque
    if saque == saque:
        break

if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de R$50')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10')
if um > 0:
    print(f'Total de {um} cédulas de R$1')
print('===' * 11)
print()
print('Volte sempre. Tenha um bom dia!')
