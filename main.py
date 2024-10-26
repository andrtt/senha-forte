import getpass

def tem_sequencia(senha, tamanho_sequencia=3):
    
    # Cria um dicionário para contar a ocorrência de cada caractere
    contador = {}
    
    for caractere in senha:
        if caractere in contador:
            contador[caractere] += 1
        else:
            contador[caractere] = 1

    # Verifica se algum caractere tem uma contagem igual ou superior a tamanho_sequencia
    for count in contador.values():
        if count >= tamanho_sequencia:
            return True
            
    return False

# Solicitar senha do usuário
senha = getpass.getpass('Senha: ')
conf_senha = getpass.getpass('Confirme sua Senha: ')

# Verificação de confirmação de senha
if senha == conf_senha:
    if tem_sequencia(senha):
        print('A senha não pode ter uma sequência de caracteres repetidos, ex: aaa, 111, e etc.')
    else:
        print('Senha salva com sucesso!')
else:
    print('As senhas não conferem.')

