from time import sleep
dados_temporarios = {}


def mostraLinha():
    print('-' * 40)


def menu(txt):
    mostraLinha()
    print(txt.center(40))
    mostraLinha()


def cadastroDePessoas():
    menu('NOVO CADASTRO')
    nome = str(input('Nome: ')).strip().title()
    while True:
        if nome.isnumeric():
            print('Erro! Por favor insira um nome válido.')
            nome = str(input('Nome: ')).strip().title()
        else:
            break
    mostraLinha()
    idade = str(input('Idade: ')).strip()
    while True:
        if idade.isalpha():
            print('Erro! Por favor insira uma idade válida.')
            idade = str(input('Idade: ')).strip()
        else:
            break
    dados_temporarios['nome'] = nome
    dados_temporarios['idade'] = idade
    print(f'Novo registro de {nome} adicionado.')
    with open('dados_pessoas.txt', 'a') as arquivo:
        for valor in dados_temporarios.values():
            arquivo.write(f'{str(valor)}\n')
    dados_temporarios.clear()


def verPessoasCadastradas():
    menu('PESSOAS CADASTRADAS')
    sleep(0.3)
    try:
        contador = 0
        with open('dados_pessoas.txt', 'r') as arquivo:
            for valor in arquivo:
                contador += 1
                teste = valor.replace('\n', ' ')
                if contador == 1:
                    print(f'{teste:<32}', end='')
                else:
                    print(f'{teste:>1}anos')
                    contador = 0
    except FileNotFoundError:
        print('Erro! Nenhuma pessoa cadastrada, por favor cadastre uma pessoas.')


def opcao(mensagem):
    while True:
        sleep(0.3)
        menu('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do programa''')
        while True:
            try:
                escolha = str(input(mensagem)).strip()
                sleep(1)
                if escolha == '' or escolha <= '0' or escolha >= '4':
                    print('ERRO! Por favor, digite um número inteiro válido.')
                else:
                    escolha = int(escolha)
                if escolha == 1:
                    verPessoasCadastradas()
                    break
                elif escolha == 2:
                    cadastroDePessoas()
                    break
                elif escolha == 3:
                    break
            except (ValueError, TypeError):
                print('ERRO! Por favor, digite um número inteiro válido.')
        if escolha == 3:
            menu('Saindo do sistema... Até logo!')
            sleep(1)
            break
