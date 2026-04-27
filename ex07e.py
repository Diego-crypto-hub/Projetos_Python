frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase: '.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) # para aparecer na posição 1
print('A última ocorrência de A apareceu na posiçâo {}'.format(frase.rfind('A')+1)) # o R serveu para contar a partir do lado esquerdo

