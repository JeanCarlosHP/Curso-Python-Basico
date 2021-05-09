from time import sleep
todos_alunos = []
nota = []
aluno = []
contador = 1
while True:
    print('--' * 20)
    print('{:>21}{}{}'.format('DADOS DO ', contador, '° ALUNO'))
    print('--' * 20)
    contador += 1
    aluno.append(str(input('Nome: ')))
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    aluno.append(nota[:])
    todos_alunos.append(aluno[:])
    nota.clear()
    aluno.clear()
    quer_continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while quer_continuar not in 'SN':
        quer_continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if quer_continuar == 'N':
        break
print('-=-' * 20)
print('No. NOME        MEDIA')
print('--' * 11)
for tabela in range(0, len(todos_alunos)):
    media = float(todos_alunos[tabela][1][0] + todos_alunos[tabela][1][1]) / 2
    print(f'{tabela}   {todos_alunos[tabela][0]:<12}', end='')
    print(f'{media:>5.1f}')
print('--' * 11)
while True:
    print('-=-' * 20)
    mostrar_notas = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if mostrar_notas == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'Notas de {todos_alunos[mostrar_notas][0]} são {todos_alunos[mostrar_notas][1][0]} e ', end='')
    print(f'{todos_alunos[mostrar_notas][1][1]}')
