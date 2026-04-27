nome = str (input ('Digite seu nome completo: ')).strip() #faz os espaços do começo e final nao aparecerem
print('Analisando seu nome é... ')
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúscula é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Aeu primeiro nome tem {} letras'.format(nome.find(' ')))

