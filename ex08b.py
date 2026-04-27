n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) /2 #lembrar a ordem das medias aritmedicas.
print('A sua média foi {:.1f}'.format(m))
if m >= 7.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua nota foi ruim! Tente na recuperação.')

    #tem a forma simplicada  ->  print('parabens!' if m >=6 else 'ESTUDE MAIS')



