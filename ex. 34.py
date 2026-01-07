sal = float(input('Qual é o salário do funcionário? R$'))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('O salário atual passará a ser de {:.2f}.'.format(novo))