n = str(input('Digite seu nome completo: ')).strip()
nome = n.split() #vai pegar o nometodo e vai separar em pedacos separados por espaços
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))



