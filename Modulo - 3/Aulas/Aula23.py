while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b
    except (ValueError, TypeError):
        print('Tivemos um problema com os tipos de dados que você digitou.')
    except ZeroDivisionError:
        print('Não é possivel dividir um número por zero!')
    except KeyboardInterrupt:
        print('O usuário prefiriu não informar dados!')
    else:
        print(f'O resultado é: {r:.1f}')
    finally:
        print('Volte sempre! Muito obrigado!')
