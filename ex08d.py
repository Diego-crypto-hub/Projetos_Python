velocidade = float(input('Qual é a velocidade atual do carro? '))
if  velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7 # a cada 10km que passar, vai custar 7 reais pra cada km ultrapassado
    print('Você deve pagar uma multa de R${:.f2}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

