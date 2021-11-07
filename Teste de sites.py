import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.youtube.com')
except urllib.error.URLError:
    print('O site nao esta acessivel no momento')
else:
    print('Conexão feita')