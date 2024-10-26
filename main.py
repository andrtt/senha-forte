import math
import getpass

senha = getpass.getpass(input('Senha:'))
conf_senha = getpass.getpass(input('Confirme sua Senha:'))

if senha == conf_senha:
    print ('Senha salva')
else:
    print ('Senhas não conferem')


