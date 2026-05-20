#Testa https
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://google.com')
except urllib.error.URLError:
    print('Erro ao tentar url')
else:
    print('OK! Site acessado com sucesso')
    print(site.read())#baixa o codigo do site