import math
import getpass

senha = str(input('Senha:'))
conf_senha = str(input('Confirme sua Senha:'))

if senha == conf_senha:
    print ('Senha salva')
else:
    print ('Senhas não conferem')

