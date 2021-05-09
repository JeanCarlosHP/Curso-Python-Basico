import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/', timeout=1)
except urllib.error.URLError:
    print('O site pudim não está acessível no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
