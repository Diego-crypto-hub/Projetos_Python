import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi,))

# HYPOT é o calculo da hipotenusa importado da biblioteca math.