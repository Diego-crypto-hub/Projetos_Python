from random import randint # serve para gerar um numero aleatorio
from time import sleep # faz o computador esperar um pouco antes de responder
computador = randint(0,5) # faz o computador sortear o numero
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))

