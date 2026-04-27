n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) /2 #lembrar sempre da ordem de precedencia.
print('A média enre: {} e {} é: {}' .format(n1, n2, m,))

# O {:.1f} serve para as casa decimais, por exemplo: {:.1} a media ficaria 8.9. {:.2f} a media ficaria 8.95.