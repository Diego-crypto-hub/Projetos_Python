from math import trunc
num = float(input('Digite um numero: '))
print ('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))


#sempre que importar algo da biblioteca, fazer o comando igual em cima *math.trunc(num)
#caso queira importar apenas um digite la em cima *from math import trunc. no format apenas *trunc(num)