salario = float (input('Qual é o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)
print ('O salário que era de R${:.2f}, com o aumento de 15% vai passar a receber R${:.2f}'.format(salario, novo))